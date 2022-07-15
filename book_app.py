import streamlit as st
import pandas as pd
import numpy as np
from recommendation_model import predict_book
from books_metadata import books_data
import hydralit_components as hc
from PIL import Image

st.set_page_config(
     page_title="Books App",
     page_icon="💡"
)
st.title('Book Recommendation APP')
# specify the primary menu definition
menu_data = [
        {'icon': "📚", 'label':"Recommend books",'ttip':"Use our advanced ML engine to find similar books"},
        {'icon': "🔍", 'label':"Search books",'ttip':"Search books from our database"}
]
# we can override any part of the primary colors of the menu
#over_theme = {'txc_inactive': '#FFFFFF','menu_background':'red','txc_active':'yellow','option_active':'blue'}
over_theme = {'txc_inactive': 'white','menu_background':'black','txc_active':'white','option_active':'blue'}
font_fmt = {'font-class':'h2','font-size':'100%'}
op = hc.option_bar(option_definition=menu_data,key='PrimaryOption',override_theme=over_theme,font_styling=font_fmt,horizontal_orientation=True)

if op=='Recommend books':

    form1 = st.empty()
    with form1.form("my_form",clear_on_submit=True):
        st.caption("Please enter the book name in the form..")
        book_name = st.text_input('Book Name..', placeholder = 'The Alchemist')
        submitted = st.form_submit_button("Submit")
    if submitted:
        books = predict_book(book_name)
        res = books.replace('A: ',"")
        books_list = list(res.split(","))
        if len(books_list)>0:
            st.success("Recommendations for your search: **_"+book_name+"_**")
            for book in books_list:
                book_meta = books_data(book)
                with st.expander(book):
                    col1, col2, col3, col4, col5, col6 = st.columns((0.5,2,0.5,2,0.5,2))
                    with col2:
                        if 'imageLinks' in book_meta:
                            st.image(
                            book_meta['imageLinks']['thumbnail'],
                            width=150 # Manually Adjust the width of the image as per requirement
                            )
                        else:
                            def_img = Image.open('./static/images/thumbnail_def.png')
                            st.image(def_img,
                            width=150)
                        if 'previewLink' in book_meta:
                            url = book_meta['previewLink']
                            st.markdown("[Preview Book](%s)" %url, unsafe_allow_html=True)
                    with col4:
                        if 'title' in book_meta:
                            st.write("**Title:** _"+book_meta['title']+"_")
                        if 'authors' in book_meta:
                            st.write("**Author:**  _"+book_meta['authors'][0]+"_")
                    with col6:
                        if 'pageCount' in book_meta:
                            st.write("**Pages:** ",book_meta['pageCount'])
                        if 'subtitle' in book_meta:
                            st.write("**Subtitle:** _"+book_meta['subtitle']+"_")
                        elif 'description' in book_meta:
                            st.write("**Description:** ",book_meta['description'][0:150])
        else:
            st.error("No recommendation found for your search: **_"+book_name+"_**")

else:
    st.write("Try again!")
            
