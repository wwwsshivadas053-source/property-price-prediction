# 🏡 Property Price Prediction System

> An intelligent **Property Price Prediction System** built with **Python, Flask, Machine Learning, Scikit-learn, SQLite, and HTML/CSS** that predicts residential property prices based on user inputs. The application includes secure user authentication, profile management, prediction history, PDF report generation, feedback management, and an admin dashboard for complete system administration.

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green?style=for-the-badge)
![Scikit Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge&logo=sqlite)
![HTML5](https://img.shields.io/badge/HTML5-orange?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-blue?style=for-the-badge&logo=css3)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

---

# 📌 Project Overview

The **Property Price Prediction System** is a Machine Learning powered web application that estimates residential property prices using property-related features entered by users.

The system provides a complete real-estate prediction platform featuring:

- 🔐 Secure User Authentication
- 👤 User Profile Management
- 🏡 Property Price Prediction
- 📊 Machine Learning Model
- 📄 Downloadable Prediction Reports (PDF)
- ⭐ User Feedback System
- 📜 Prediction History
- 👨‍💼 Admin Dashboard
- 👥 User Management
- 📈 Prediction Analytics

The application follows a clean architecture using Flask as the backend and Scikit-learn for machine learning.

---

# 🚀 Features

## 👤 User Module

- User Registration
- Secure Login
- Password Encryption
- Forgot Password
- OTP Verification
- Reset Password
- User Profile
- Logout

---

## 🏡 Property Price Prediction

Users can predict house prices by entering property details such as:

- Area
- Bedrooms
- Bathrooms
- Stories
- Parking
- Main Road Access
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Preferred Area
- Furnishing Status

The trained Machine Learning model instantly predicts the estimated property price.

---

## 📄 PDF Report Generation

The application generates downloadable PDF reports containing:

- Property Details
- Predicted Price
- Prediction Date
- User Information

---

## ⭐ Feedback System

Users can:

- Submit Feedback
- Share Suggestions
- Report Issues

Admins can manage all submitted feedback.

---

## 👨‍💼 Admin Panel

Administrator functionalities include:

- Admin Login
- Dashboard
- Manage Users
- View Predictions
- Manage Feedback
- Monitor System Usage

---

# 🧠 Machine Learning

The project uses **Scikit-learn** for training the prediction model.

### Workflow

```
Housing Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Encoding
        │
        ▼
Train ML Model
        │
        ▼
Save Model (.pkl)
        │
        ▼
Flask Prediction API
        │
        ▼
Price Prediction
```

---

# 🛠 Tech Stack

## Backend

- Python
- Flask

## Machine Learning

- Scikit-learn
- NumPy
- Pandas
- Pickle

## Database

- SQLite

## Frontend

- HTML5
- CSS3
- JavaScript

## Reporting

- ReportLab (PDF)

## Deployment

- Gunicorn
- Render

---

# 📂 Project Structure

```
property_price_prediction/
│
├── app.py
├── train_model.py
├── create_db.py
├── test.py
│
├── Housing.csv
├── model.pkl
├── encoder.pkl
├── database.db
│
├── requirements.txt
├── build.sh
├── Procfile
│
├── static/
│   └── css/
│       ├── style.css
│       └── admin.css
│
├── templates/
│   ├── home.html
│   ├── login.html
│   ├── register.html
│   ├── profile.html
│   ├── prediction.html
│   ├── prediction_result.html
│   ├── dashboard.html
│   ├── feedback.html
│   ├── admin_login.html
│   ├── admin_dashboard.html
│   ├── manage_users.html
│   ├── manage_predictions.html
│   ├── manage_feedback.html
│   ├── forgot_password.html
│   ├── verify_otp.html
│   └── reset_password.html
│
└── README.md
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/property-price-prediction.git

cd property-price-prediction
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create Database

```bash
python create_db.py
```

---

## Train Model (Optional)

```bash
python train_model.py
```

---

## Run Application

```bash
python app.py
```

Application will start at

```
http://127.0.0.1:5000
```

---

# 📦 Requirements

```
Flask
numpy
pandas
scikit-learn
Werkzeug
reportlab
gunicorn
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 🔒 Authentication

The system implements:

- Password Hashing
- Session Management
- Login Authentication
- Logout Protection
- Role-based Admin Access

---

# 📊 Prediction Workflow

```
User Login

      │

      ▼

Enter Property Details

      │

      ▼

ML Model Prediction

      │

      ▼

Predicted Property Price

      │

      ▼

Save Prediction

      │

      ▼

Download PDF Report
```

---

# 🎯 Future Improvements

- Google Maps Integration
- Location-based Predictions
- Property Image Upload
- Price Trend Analysis
- AI Price Recommendation
- Deep Learning Models
- Email Reports
- SMS Notifications
- REST API
- Mobile Application
- Cloud Database
- Interactive Charts
- Advanced Analytics

---

# 📸 Screenshots

## 🏠 1. Home Page

<img width="1366" alt="Home" src="https://github.com/user-attachments/assets/1a8e721f-9151-4c08-85b3-f08a53fcfaa2" />

---

## 📝 2. User Registration

<img width="1366" alt="Registration" src="https://github.com/user-attachments/assets/c99a34de-6d2c-4209-a4d3-38e9b24e4b1b" />

---

## 🔐 3. User Login

<img width="1366" alt="Login" src="https://github.com/user-attachments/assets/3b3436cb-7e19-4ff4-9305-16194d7cee1b" />

---

## 👤 4. User Profile

<img width="1351" alt="Profile" src="https://github.com/user-attachments/assets/9c965975-e737-450e-bfe3-c68814d6909b" />

---

## 🏡 5. Property Price Prediction Form

<img width="1353" alt="Prediction Form" src="https://github.com/user-attachments/assets/d66368be-4d16-4e32-a926-fed7045c1f8c" />

---

## 📈 6. Prediction Result

<img width="1358" alt="Prediction Result" src="https://github.com/user-attachments/assets/7325643b-6091-49cd-bb69-2f098d24b68a" />

---

## 📊 7. Prediction History

<img width="1351" alt="Prediction History" src="https://github.com/user-attachments/assets/b64d34c3-1d7a-4df0-aae8-e3d4d5f5b7e2" />

---

## 📄 8. Prediction Report / Details

<img width="1357" alt="Prediction Details" src="https://github.com/user-attachments/assets/20534bdc-d743-426c-960b-f0490940c0f8" />

---

## ⭐ 9. Feedback Form

<img width="1356" alt="Feedback" src="https://github.com/user-attachments/assets/abc4855c-7f1c-470e-9331-90ef93e4047c" />

---

## ✅ 10. Feedback Submitted

<img width="1355" alt="Feedback Success" src="https://github.com/user-attachments/assets/6561a7b6-83f0-4f8b-a1a6-04b529710683" />

---

# 👨‍💼 Admin Panel

## 🔐 11. Admin Login

<img width="1366" alt="Admin Login" src="https://github.com/user-attachments/assets/97131a49-3cd0-4250-9e17-8a60a2ba928c" />

---

## 📊 12. Admin Dashboard

<img width="1356" alt="Admin Dashboard" src="https://github.com/user-attachments/assets/893f8eef-0152-4e32-a3d5-31b968deb33a" />

---

## 👥 13. Manage Users

<img width="1366" alt="Manage Users" src="https://github.com/user-attachments/assets/29736058-74e2-4006-ac00-3149fbc2679d" />

---

## 🏠 14. Manage Predictions

<img width="1358" alt="Manage Predictions" src="https://github.com/user-attachments/assets/334f4b97-1d0d-4b36-9e87-20424ed7e4fe" />

---

## 💬 15. Manage Feedback

<img width="1352" alt="Manage Feedback" src="https://github.com/user-attachments/assets/5cfdc3c2-5692-4f60-8d03-c45b83b6c288" />

---
# 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new feature branch

```bash
git checkout -b feature/NewFeature
```

3. Commit changes

```bash
git commit -m "Added new feature"
```

4. Push changes

```bash
git push origin feature/NewFeature
```

5. Open a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Prajwal T.S.**

- GitHub: https://github.com/wwwsshivadas053-source
- LinkedIn: https://www.linkedin.com/in/prajwal-t-s-354a57359

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub. Your support helps improve and maintain the project.

---

## 💡 Keywords

Property Price Prediction • House Price Prediction • Machine Learning • Flask • Python • Scikit-learn • SQLite • Real Estate Prediction • AI • Housing Price Estimation • Regression Model • Data Science • Prediction System
