# Property Price Prediction System
Overview

The Property Price Prediction System is a Flask-based web application that predicts house prices based on property features using Machine Learning. The application allows users to estimate property values, generate PDF reports, and manage prediction records through a user-friendly interface.

Features
Property price prediction using Machine Learning
User registration and login system
Property details input form
Real-time price estimation
PDF report generation
Prediction history management
Responsive user interface
SQLite database integration
Email notification support
Technologies Used
Frontend
HTML5
CSS3
Bootstrap 5
JavaScript
Backend
Python
Flask
SQLite
Machine Learning
Scikit-Learn
Pandas
NumPy
Additional Libraries
ReportLab (PDF Generation)
Werkzeug
Gunicorn
Project Structure
property_price_prediction/
│
├── app.py
├── create_db.py
├── database.db
├── model.pkl
├── encoder.pkl
├── Housing.csv
├── requirements.txt
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── prediction.html
│   └── history.html
│
└── README.md
Installation
Clone the Repository
git clone https://github.com/your-username/property-price-prediction.git
cd property-price-prediction
Create Virtual Environment
python -m venv venv
Activate Virtual Environment

Windows:

venv\Scripts\activate

Linux/Mac:

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Run the Application
python app.py

Open your browser and visit:

http://127.0.0.1:5000
Deployment on Render
Build Command
pip install -r requirements.txt
Start Command
gunicorn app:app
Environment Variables
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password
Machine Learning Model

The model is trained using housing data and predicts property prices based on:

Area
Number of Bedrooms
Number of Bathrooms
Stories
Parking Availability
Furnishing Status
Main Road Access
Air Conditioning
Preferred Area
Additional Property Features
Future Enhancements
Advanced property analytics
Interactive charts and graphs
Property comparison feature
AI-powered recommendations
Location-based price prediction
Cloud database integration
Admin dashboard
Author

Prajwal T.S.

Bachelor's Degree Graduate
Aspiring AI & Machine Learning Engineer

License

This project is developed for educational and learning purposes.
