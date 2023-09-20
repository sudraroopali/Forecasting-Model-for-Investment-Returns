
import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page

# Bold title
st.title("**What is Investing?**")

    # Information about investing
st.write("Investing is the process of allocating your money with the expectation of earning a profit or achieving a financial goal. It involves purchasing assets such as stocks, bonds, real estate, or mutual funds with the hope that they will increase in value over time.")

    # Bold "Benefits of Investing" header
st.header("**Benefits of Investing:**")

    # Bullet points
st.write("- Potential for long-term growth.")
st.write("- Diversification of your financial portfolio.")
st.write("- Building wealth and achieving financial security.")

if st.button("Learn about the Types of Investments"):
    switch_page("thirdpage")
