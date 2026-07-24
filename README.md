# 🩺 MIRA - AI Patient Health Risk Prediction Dashboard

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00.svg)](https://www.tensorflow.org/)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000.svg)](https://keras.io/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C.svg)](https://matplotlib.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)]()

A machine learning-powered healthcare dashboard built with **Streamlit**, **Scikit-learn**, and **SQLite** for patient intake, health risk prediction, and medical record management.

---

## Overview

MIRA is an intelligent healthcare application designed to simplify patient registration and assist healthcare professionals by providing AI-based risk assessments from basic laboratory measurements.

The application allows users to:

- Register new patients
- Validate patient information
- Store records securely in SQLite
- Predict potential health risks using Machine Learning
- Display all patient records in an interactive dashboard

---

## Features

- Patient Registration System
- Real-time Input Validation
- AI-based Health Risk Prediction
- Decision Tree Machine Learning Model
- SQLite Database Integration
- Interactive Streamlit Dashboard
- Patient Record Management
- Delete Existing Records
- Responsive User Interface

---

# Project Architecture

```

User Input
│
▼
Input Validation
│
▼
Feature Processing
│
▼
Decision Tree ML Model
│
▼
Risk Prediction
│
▼
SQLite Database
│
▼
Interactive Dashboard

```

---

# Machine Learning Workflow

```

Synthetic Dataset Generation
↓
Feature Engineering

- Glucose
- Haemoglobin
- Cholesterol

↓

Decision Tree Training

↓

Model Prediction

↓

Health Risk Classification

```

---

## Health Risk Categories

| Prediction | Description |
|------------|-------------|
| High Risk | Metabolic and cardiovascular abnormalities detected |
| Elevated Diabetes Risk | High blood glucose level |
| Suspected Anemia | Low haemoglobin level |
| High Cholesterol Risk | Elevated cholesterol |
| Stable | Normal laboratory measurements |

---

# Technologies Used

## Programming

- Python

## Machine Learning

- Scikit-learn
- Decision Tree Classifier

## Data Processing

- NumPy
- Pandas

## Frontend

- Streamlit

## Database

- SQLite

---

# Project Structure

```

mira-health-risk-predictor/
│
├── app.py
├── mira_patient_records.db
├── requirements.txt
├── README.md
├── LICENSE
│
└── screenshots/
├── dashboard.png
├── prediction.png
└── database.png

```

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/mira-health-risk-predictor.git
```

Move into project directory

```bash
cd mira-health-risk-predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

# Input Parameters

The model accepts three medical laboratory measurements:

- Blood Glucose (mg/dL)
- Haemoglobin (g/dL)
- Cholesterol (mg/dL)

These values are processed by the Decision Tree model to generate an AI-assisted health risk prediction.

---

# Validation Rules

- Name cannot be empty
- Date of birth must be in the past
- Valid email address required
- Biomarker values must be positive

---

# Future Enhancements

- User Authentication
- Doctor Login Portal
- Patient Search
- PDF Medical Report Generation
- Email Notifications
- Cloud Database Integration
- Model Performance Evaluation
- Medical Image Support
- REST API Deployment
- Docker Containerization

---

# Learning Outcomes

This project demonstrates practical implementation of:

- Machine Learning Classification
- Healthcare Data Processing
- Feature Engineering
- Streamlit Web Development
- SQLite Database Operations
- Data Validation
- CRUD Operations
- Model Integration
- End-to-End ML Application Development

---

# License

This project is licensed under the MIT License.

---

## Author

**M. Chandra Sekhar**

Artificial Intelligence & Data Science Graduate

Machine Learning | Data Science | Python | SQL | Streamlit
