import sqlite3
import re
from datetime import date
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier

# ==========================================
# 1. DATABASE SETUP
# ==========================================
DB_NAME = "mira_patient_records.db"

def init_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, dob TEXT, email TEXT,
            glucose REAL, haemoglobin REAL, cholesterol REAL, remarks TEXT
        )
    ''')
    conn.commit()
    conn.close()

init_database()

# ==========================================
# 2. REAL MACHINE LEARNING LOGIC (In-Memory Training)
# ==========================================
@st.cache_resource
def train_local_ml_model():
    """Generates synthetic training data and trains an ML Classifier on the fly."""
    np.random.seed(42)
    # Generate 500 fake health records to train on
    mock_glucose = np.random.uniform(50, 200, 500)
    mock_haemoglobin = np.random.uniform(8, 18, 500)
    mock_cholesterol = np.random.uniform(120, 300, 500)
    
    # Define targets mathematically
    mock_labels = []
    for g, h, c in zip(mock_glucose, mock_haemoglobin, mock_cholesterol):
        if g > 125 and c > 200: mock_labels.append(0) # High Risk: Metabolic/Cardio
        elif g > 125: mock_labels.append(1)          # Risk: Elevated Diabetes
        elif h < 12.0: mock_labels.append(2)         # Risk: Suspected Anemia
        elif c > 200: mock_labels.append(3)          # Risk: High Cholesterol
        else: mock_labels.append(4)                  # Normal baseline
        
    X = pd.DataFrame({'glucose': mock_glucose, 'haemoglobin': mock_haemoglobin, 'cholesterol': mock_cholesterol})
    y = np.array(mock_labels)
    
    model = DecisionTreeClassifier(max_depth=4, random_state=42)
    model.fit(X, y)
    return model

# Train the ML model when the app starts up
ml_model = train_local_ml_model()

def get_ml_prediction(glucose, haemoglobin, cholesterol):
    # Format input for the ML model
    input_data = pd.DataFrame([[glucose, haemoglobin, cholesterol]], columns=['glucose', 'haemoglobin', 'cholesterol'])
    prediction_id = ml_model.predict(input_data)[0]
    
    # Map ML outputs to the final clinical "Remarks"
    mapping = {
        0: "ML Prediction: High Risk. Combined signs of metabolic and cardiovascular strain.",
        1: "ML Prediction: Elevated Diabetes Risk. High glucose levels detected.",
        2: "ML Prediction: Suspected Anemia. Low haemoglobin levels detected.",
        3: "ML Prediction: High Cholesterol Risk. Cardiovascular monitoring advised.",
        4: "ML Prediction: Stable. Lab metrics fall within normal operational baselines."
    }
    return mapping.get(prediction_id, "ML Prediction: Analysis complete. Baseline normal.")

# ==========================================
# 3. INTERFACE LAYOUT
# ==========================================
st.set_page_config(page_title="MIRA Intake Engine", layout="wide")
st.title("🩺 MIRA - Patient Health Dashboard & AI Predictor")
st.markdown("---")

left_col, right_col = st.columns([1, 1.2])

with left_col:
    st.subheader("📥 Patient Intake Form")
    with st.form("patient_form", clear_on_submit=True):
        full_name = st.text_input("Full Name")
        dob = st.date_input("Date of Birth", max_value=date.today())
        email = st.text_input("Email Address")
        
        st.markdown("**Lab Results Panel**")
        glucose = st.number_input("Glucose (mg/dL)", min_value=0.0, step=1.0)
        haemoglobin = st.number_input("Haemoglobin (g/dL)", min_value=0.0, step=0.1)
        cholesterol = st.number_input("Cholesterol (mg/dL)", min_value=0.0, step=1.0)
        
        submit = st.form_submit_button("Save Record & Run AI")

    if submit:
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        if not full_name:
            st.error("❌ Validation Error: Name cannot be blank.")
        elif dob >= date.today():
            st.error("❌ Validation Error: Birthdate must be a past date.")
        elif not re.match(email_pattern, email):
            st.error("❌ Validation Error: Please input a valid email structure.")
        elif glucose <= 0 or haemoglobin <= 0 or cholesterol <= 0:
            st.error("❌ Validation Error: Biomarkers must be positive values.")
        else:
            # Generate remarks using the real ML model!
            ai_remarks = get_ml_prediction(glucose, haemoglobin, cholesterol)
            
            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO patients (name, dob, email, glucose, haemoglobin, cholesterol, remarks)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (full_name, str(dob), email, glucose, haemoglobin, cholesterol, ai_remarks))
            conn.commit()
            conn.close()
            st.success(f"✅ Record for {full_name} captured successfully!")
            st.rerun()

with right_col:
    st.subheader("📋 Active Patient Records Directory")
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql_query("SELECT * FROM patients", conn)
    conn.close()
    
    if df.empty:
        st.info("The application database is currently empty. Input data to build records.")
    else:
        for index, row in df.iterrows():
            with st.container(border=True):
                c1, c2, c3 = st.columns([1.2, 2, 0.6])
                with c1:
                    st.markdown(f"**👤 {row['name']}**")
                    st.caption(f"DOB: {row['dob']} | Email: {row['email']}")
                with c2:
                    st.markdown(f"**Lab Data:** G: {row['glucose']} | H: {row['haemoglobin']} | C: {row['cholesterol']}")
                    st.warning(f"🤖 {row['remarks']}")
                with c3:
                    if st.button("🗑️ Delete", key=f"del_{row['id']}"):
                        conn = sqlite3.connect(DB_NAME)
                        cursor = conn.cursor()
                        cursor.execute("DELETE FROM patients WHERE id = ?", (row['id'],))
                        conn.commit()
                        conn.close()
                        st.rerun()
