# Predictive Model for Investment Returns

## Overview

This project aims to revolutionize how individuals approach investment decisions by offering an accurate and accessible tool for estimating investment returns across various types of investments. Through the integration of historical data and predictive models, this project seeks to bridge the gap between financial complexity and everyday investors.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Data](#data)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Feature Engineering](#feature-engineering)
- [Model Building](#model-building)
- [Model Evaluation](#model-evaluation)
- [Model Selection](#model-selection)
- [Model Deployment](#model-deployment)
- [Web Application](#web-application)
- [Conclusion](#conclusion)
- [Future Work](#future-work)


## Features

- Investment return estimation for various investment types.
- User-friendly web application.
- Access to historical investment data.

## Technologies Used

- Python
- Scikit-learn
- Pandas
- Streamlit
- Render (for deployment)

## Data

- Datasets from financial sources.
- Columns: Investment type, amount, tenure, price, transaction fees, market volatility, inflation rate, GDP rate, maturity amount.

## Data Preprocessing

- Data cleaning and standardization.
- Encoding categorical columns.
- Handling missing values.
- Scaling and normalization.
- Transformation on the maturity column.

## Exploratory Data Analysis (EDA)

- Visualizations and insights into the data.
- Correlation analysis.
- Patterns and trends exploration.

## Feature Engineering

- Enhancing dataset with relevant features.

## Model Building

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor
- Decision Tree Regressor
- AdaBoost Regressor

## Model Evaluation

- Metrics: R-squared, RMSE.
- Model comparison and selection.

## Model Selection

- Chose AdaBoost Regressor for final model.

## Model Deployment

- Deployed using Render.
- Web application for investment return estimation.

## Web Application

- Purpose: To predict investment returns.
- Features: Input investment parameters (amount, risk level, tenure, type), get estimated returns.

## Conclusion

- Empowered investors with a user-friendly tool for better investment decisions.
- Addressed a critical issue in investment estimation.

## Future Work

- Improve model robustness.
- Enhance user experience.
- Expand investment type options.
