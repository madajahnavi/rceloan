
import streamlit as st
import joblib
clf = joblib.load("joblib(1).csv")
st.title('LOAN APP RCE')
g=st.number_input('Enter Gender 0:Male 1:Female')
m=st.number_input('Enter Marital status 0:No 1:Yes')
ai=st.number_input('Enter Applicant income in thousands')
la=st.number_input('Enter loan amount in thousands')
if st.button('PREDICT'):
    prediction=clf.predict([[g,m,ai,la]])
    if prediction=='Y':
        st.text('LOAN IS APPROVED')
    else:
        st.text('LOAN IS REJECTED')
