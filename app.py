import streamlit as st

from pages.manual_entry import show as manual

from pages.csv_upload import show as csv_page

st.set_page_config(
    page_title="Student Marks Predictor",
    layout="wide"
)

st.title(
    "Student Marks Prediction System"
)

option = st.sidebar.radio(
    "Choose Option",
    [
        "Manual Entry",
        "CSV Upload"
    ]
)

if option == "Manual Entry":
    manual()

else:
    csv_page()