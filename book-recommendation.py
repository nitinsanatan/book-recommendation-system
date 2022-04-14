from click import prompt
import streamlit as st
import pandas as pd
import numpy as np
import openai
def predictBook(bookName):


    openai.api_key = "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"

    start_sequence = "\nA:"
    restart_sequence = "\n\nQ: "

    response = openai.Completion.create(
    engine="davinci",
    prompt="I am a highly intelligent book recommendation bot. If you give me a book, I will recommend similar books. If you give me a book outside my database, I will respond with \"Unknown\".\n\nQ: The alchemist?\nA: Eleven Minutes, The Little Prince, All the Light we cannot See\n\nQ: The Da Vinci Code?\nA: Gone Girl, In Cold Blood, Inferno\n\nQ: Pet Sematary?\nA: House Of Leaves, The Silent Companions, The Troops\n\nQ: Ramayana?\nA: Mahabharata, Ramcharitmanas, Bhagwat Geeta\n\nQ: Quran?\nA: Torah, Bible, Psalms\n\nQ: Inferno?\nA: The Da Vinci Code, Gone Girl, In Cold Blood\n\nQ: Angel and Demons?\nA: The Da Vinci Code, Gone Girl, In Cold Blood\n\nQ: Rich Dad Poor Dad?\nA: The Millionaire Fastlane, The Millionaire Mind, The Millionaire Real Estate Investor\n\nQ: 2 States?\nA: 5 Point Someone, One Night @ the Call Center, Revolution 2020\n\nQ: Bird Box? \nA: The Haunting of Hill House, The Shining, The Girl with All the Gifts\n\nQ: Home Before Dark?\nA: The Haunting of Hill House, House of Leaves, It\n\nQ: It?\nA: The Haunting of Hill House, House of Leaves, Home Before Dark\n\nQ: Rigveda?\nA: Yajurveda, Samveda, Atharvaveda\n\nQ: The monk who sold ferrari?\nA: The Alchemist, The Power of Now, The Art of Happiness\n\nQ: You are the best friend?\nA: You are the best wife, the boy who loved, Her last wish\n\nQ: The Perfect Us?\nA: The boy who loved, If it's not forever, 2 states\n\nQ: When Dimple met Rishi?\nA: From Twinkle, with love, If you're reading this it's too late, Simon vs. the Homo Sapiens Agenda\n\nQ: What if it's us?\nA: If you're reading this it's too late, Simon vs. the Homo Sapiens Agenda, The Fault in Our Stars\n\nQ: Torah?\nA: Quran, Bible, Psalms\n\nQ: Gospel?\nA: Bible, Quran, Psalms\n\nQ: Vedas?\nA: Rigveda, Yajurveda, Samaveda, Atharvaveda\n\nQ: Gulliver's Travel?\nA: Around the World in Eighty Days, Journey to the Center of the Earth, The Adventures of Huckleberry Finn\n\nQ: The canterville ghost?\nA: The Haunting of Hill House, The Shining, The Girl with All the Gifts\n\nQ: Harry Potter and the Chamber of Secrets?\nA: Harry Potter and the Philosopher's Stone, Harry Potter and the Goblet of Fire, Harry Potter and the Order of the Phoenix\n\nQ: The invisible man?\nA: The Haunting of Hill House, The Shining, The Girl with All the Gifts\n\nQ: The Story of my life?\nA: The Diary of a Young Girl, The Autobiography of Malcolm X, I Know Why the Caged Bird Sings\n\nQ: Steve Jobs?\nA: Walter Isaacson, The Innovators, Steve Jobs\n\nQ: brief answers to the big questions?\nA: The world as I see it, cosmos, The grand design\n\nQ: A brief history of time?\nA: The Elegant Universe, A Universe from Nothing, The Fabric of the Cosmos\n\nQ: Never too big to fail?\nA: The Big Short, The Outsiders, Too Big to Fail\n\nQ: ",
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
    )
    st.write(response)
st.title('Book Recommendation APP')

form1 = st.empty()
with form1.form("my_form",clear_on_submit=True):
    st.caption("Please enter the book name in the form..")
    bookName = st.text_input('Book Name..', placeholder = 'The Alchemist')
    submitted = st.form_submit_button("Submit")
if submitted:
    predictBook(bookName)
