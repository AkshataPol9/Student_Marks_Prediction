
import streamlit as st
import pandas as pd
import pickle

with open("student_marks_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Student Marks Prediction")
st.write("Enter student details to predict final marks.")

hours = st.number_input("Hours Studied", min_value=0, value=5)
attendance = st.number_input("Attendance (%)", min_value=0, max_value=100, value=85)
previous_marks = st.number_input("Previous Marks", min_value=0, value=70)
sleep = st.number_input("Sleep Hours", min_value=0, value=7)
practice = st.number_input("Practice Tests", min_value=0, value=4)

extra = st.selectbox("Extracurricular Activities", ["Yes", "No"])

if st.button("Predict Marks"):
    new_student = pd.DataFrame({
        "Hours_Studied": [hours],
        "Attendance": [attendance],
        "Previous_Marks": [previous_marks],
        "Sleep_Hours": [sleep],
        "Practice_Tests": [practice],
        "Extracurricular": [1 if extra == "Yes" else 0]
    })

    prediction = model.predict(new_student)
    st.success(f"Predicted Final Marks: {prediction[0]:.2f}")
