# realtor.com_housepricing
🏡 Realtor.com House Price Prediction

An End-to-End Big Data & Machine Learning Web Application

📌 Project Overview

This project builds a full data pipeline for predicting house prices using real estate listings scraped from Realtor.com.
It covers the complete lifecycle of a data-driven application:

🌐 Web scraping real estate data

🗄️ Storing raw data in MongoDB

🧹 Data cleaning & feature engineering

🤖 Machine learning model training

📦 Model serialization with Pickle

🚀 Deployment of a Flask web application for real-time predictions

The final result is a user-friendly web app where users can input house features and receive a predicted house price instantly.

Web Scraping (Realtor.com)
        ↓
MongoDB (Raw Listings)
        ↓
Data Cleaning & Preprocessing
        ↓
Feature Engineering
        ↓
Machine Learning Model
        ↓
Pickle Serialization
        ↓
Flask Web Application
        ↓
Web Deployment


🌐 1. Web Scraping
Objective

Collect real estate listings data such as:

House size (sqm)

Number of bedrooms

Number of bathrooms

Lot size

Price

Tools & Techniques

Python

requests

BeautifulSoup

selenium

HTML parsing and pagination handling

Output

Structured JSON-like records for each property listing

🗄️ 2. Database Storage (MongoDB)
Why MongoDB?

Handles semi-structured scraped data easily

Scalable for large datasets

Flexible schema during early data collection

Process

Scraped data is stored in MongoDB collections

Each document represents one property listing

Example of data: 
{
  "sqm": 234.77,
  "beds": 4,
  "baths": 2.5,
  "sqm_lot": 602.94,
  "price": 450000
}


🧹 3. Data Cleaning & Preprocessing

Once data is collected, it is exported from MongoDB and processed using:

Pandas

NumPy

Steps

Handling missing values

Removing outliers

Converting units (where necessary)

Ensuring numeric consistency

Feature selection

🧠 4. Feature Engineering

Selected features used for prediction:

Feature	Description
sqm	House size in square meters
beds	Number of bedrooms
baths	Number of bathrooms
sqm_lot	Lot size in square meters
Scaling

StandardScaler is applied to normalize features

Prevents model bias due to feature magnitude differences

🤖 5. Machine Learning Model
Model Used

Linear Regression

Libraries

scikit-learn

Training Process

Train-test split

Feature scaling

Model training

Performance evaluation using R² score

Output

A trained regression model capable of predicting house prices

📦 6. Model Serialization

To ensure consistent predictions in production:

The model

The scaler

The feature list

are bundled into a single file using Pickle.

Saved File
reg_model4.pkl


This guarantees:

Same preprocessing as training

Correct feature order

Reliable predictions

🌐 7. Flask Web Application
Backend

Built using Flask

Loads the serialized model package

Handles:

Web page rendering

API predictions

Form submissions

Routes
Route	Method	Description
/	GET	Home page
/predict	POST	Form-based prediction
/predict_api	POST	JSON API prediction
🎨 8. Frontend (HTML & CSS)
Features

Clean UI with a real estate-themed background

Responsive card-based layout

User-friendly input form

Real-time price display

Technologies

HTML5

CSS3

Jinja2 (Flask templating)

🚀 9. Deployment
Local Deployment
python app.py


App runs on:

http://127.0.0.1:5000

Production-Ready Capabilities

This application can be deployed on:

Render

Railway

Heroku

AWS EC2

With:

Gunicorn

Environment-based configuration

Scalable architecture

🛠️ Tech Stack Summary
Layer	Tools
Scraping	Python, BeautifulSoup
Database	MongoDB
Processing	Pandas, NumPy
ML	Scikit-learn
Backend	Flask
Frontend	HTML, CSS
Serialization	Pickle
Deployment	Render / AWS / Railway
🎯 Conclusion

This project demonstrates a complete big data & machine learning workflow, transforming raw web data into a production-ready predictive web application. It highlights practical skills in:

Data engineering

Machine learning

Backend development

Web deployment

👤 Author

Mr_Life(Ikenna Ogenyi)
Big Data Final Project


📅 Date
2023-12-10