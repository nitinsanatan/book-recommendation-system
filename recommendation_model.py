import streamlit as st
import openai
import pickle

def predict_book(book_name):

    openai.api_key = st.secrets["OPENAI_API_KEY"]

    with open('fine_tuned_model.pkl', 'rb') as file:  
        gpt_model = pickle.load(file)

    model_prompt = gpt_model['fine_tuned_model']
    predict_seq = model_prompt + book_name + "?\n"

    start_sequence = "\nA:"
    restart_sequence = "\n\nQ: "

    response = openai.Completion.create(
    engine="davinci",
    prompt= predict_seq,
    temperature=0,
    max_tokens=100,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["\n"]
    )
    
    return response['choices'][0]['text']