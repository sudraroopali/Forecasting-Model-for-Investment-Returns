import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.switch_page_button import switch_page


st.set_page_config(layout = "wide")



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

st.markdown("## TYPES OF INVESTMENTS")


c1, c2, c3, c4, c5 = st.columns(5)


investment_options = {
        "Stocks": "Investing in stocks means buying shares of a company's ownership. Stocks offer the potential for high returns but come with higher risk.",
        "Mutual Funds": "Mutual funds pool money from multiple investors to invest in a diversified portfolio of stocks, bonds, or other assets.",
        "Gold": "Investing in gold can be a hedge against inflation and economic uncertainty. It's a tangible asset that holds its value over time.",
        "Bonds": "Bonds are debt securities where you lend money to an issuer (government or corporation) in exchange for periodic interest payments and the return of the bond's face value.",
        "Debentures": "Debentures are similar to bonds but are not backed by collateral. They offer fixed interest payments and are typically issued by corporations.",
    }
with c1 : 
    st.info(f"**Stocks**: {investment_options['Stocks']}") 

with c2 : 
    st.info(f"**Mutual Funds**: {investment_options['Mutual Funds']}") 

with c3 : 
    st.info(f"**Gold**: {investment_options['Gold']}") 

with c4 : 
    st.info(f"**Bonds**: {investment_options['Bonds']}") 

with c5 : 
    st.info(f"**Debentures**: {investment_options['Debentures']}") 


    # Explanation about the predictive model
st.write(
        "We have created a predictive model that will help you explore different types of investments. "
        "Please note that this is for educational purposes only and not financial advice."
    )

# Ready to Explore Investments button on the second page
if st.button("READY TO EXPLORE INVESTMENTS"):
  switch_page("fourthpage")    


  