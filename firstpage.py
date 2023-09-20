import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page
import requests
import json
from streamlit_lottie import st_lottie





# Set the page title and icon
st.set_page_config(page_title="Investment App", page_icon="💰")

# Add custom CSS to change the background color
st.markdown(
    """
    <style>
    body {
        background-color: #016180; /* Change this color to your desired background color */
    }
    </style>
    """,
    unsafe_allow_html=True
)



# Center-align the content
st.markdown(
    """
    <style>
    .main {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("# Welcome to our Investment Education Website!")

st.write(
    "We've built this website as part of our capstone project to help you gain a better understanding of investing. "
    "By exploring the content here, you'll learn about the fundamentals of investing and its benefits."
)

# Ask for the customer's name
customer_name = st.text_input("Please enter your name:")

if customer_name:
    st.session_state.customer_name = customer_name

    # Display a bold question
    st.write(f"**{customer_name}**, are you ready to learn about investing and explore some cool options?")

# "I am ready" button to navigate to the next page
    if st.button("I AM READY"):
     switch_page("secondpage")

#adding the gif 

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


gif1 = load_lottieurl("https://lottie.host/6b316d83-3fa5-43e5-936c-89aa636cbf1e/dOgJkex8cT.json")

st.lottie(
        gif1,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height=300,
        width=600,
        key=None,
    )