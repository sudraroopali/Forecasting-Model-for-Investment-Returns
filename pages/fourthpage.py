import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import AdaBoostRegressor
from scipy import stats
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split



# 1. Investment Amount

_,col1, col2,_ = st.columns([0.5,1,2,1])

with col1:
    st.write("##")
    st.write(f"""<p style="margin-left: 55px;"> Investment Amount :</p>""",unsafe_allow_html=True)
with col2:
    investment_amt = st.text_input("")


#2. Investment type 

_,col3, col4, _ = st.columns([0.5,1,2,1])

with col3:
    st.write("##")
    st.write(f"""<p style="margin-left: 55px;">Investment type :</p>""",unsafe_allow_html=True)
with col4:
    investment_type = st.selectbox("", ["Gold","Mutual Funds","Bonds","Debentures","Stocks"], index=0)



#risk level 

_,col5, col6, _ = st.columns([0.5,1,2,1])

with col5:
    st.write("##")
    st.write(f"""<p style="margin-left: 55px;">Risk Level :</p>""",unsafe_allow_html=True)
with col6:
    risk_level = st.selectbox("", ["Low Risk","Medium Risk","High Risk"], index=0)


#tenure

tenure = st.slider("Select Tenure (in years):", min_value=1, max_value=20, value=20)



df = pd.read_csv("final_data.csv")

# Independent variables
X = df.drop(['MATURITY AMOUNT', 'MATURITY AMOUNT1','YEAR','PRICE','MARKET VOLATILITY','INFLATION RATE','GDP RATE','TRANSACTION FEES'], axis=1) 


#Dependent variable
y = df['MATURITY AMOUNT1']

X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=10,test_size=0.30)


model = AdaBoostRegressor().fit(X_train,y_train)

risk_level = 0 if risk_level == "Low Risk" else 1 if risk_level == "Medium Risk" else 2
bond = 1 if investment_type == "Bonds" else 0
debentures = 1 if investment_type == "Debentures" else 0
gold = 1 if investment_type == "Gold" else 0
mutual_funds = 1 if investment_type == "Mutual Funds" else 0
stocks = 1 if investment_type == "Stocks" else 0

unscaled_data = pd.read_csv('eda_data.csv')

investment_scaler = MinMaxScaler()
investment_scaler.fit_transform(unscaled_data[["INVESTMENT AMOUNT"]])

tenure_scaler = MinMaxScaler()
tenure_scaler.fit_transform(unscaled_data[["TENURE"]])

maturity_column = unscaled_data['MATURITY AMOUNT']

if st.button("ESTIMATE MY RETURNS"):
    investment_amount = investment_scaler.transform(np.array(int(investment_amt)).reshape(1,-1))
    tenure = tenure_scaler.transform(np.array(tenure).reshape(1,-1))
    user_input = np.array([investment_amount[0][0],tenure[0][0], risk_level, bond, debentures, gold, mutual_funds, stocks]).reshape(1,-1)
    maturity_amount = model.predict(user_input)
    transformed_data, lambda_value = stats.boxcox(maturity_column +1)
    predicted_value = (maturity_amount * lambda_value + 1) ** (1 / lambda_value)
    # st.write(user_input)
    # st.write(maturity_amount)
    st.write(predicted_value)
