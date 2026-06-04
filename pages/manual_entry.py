import streamlit as st

from utils.prediction import predict_marks
from utils.recommendation import subject_analysis
from utils.plotting import subject_plot
import matplotlib.pyplot
def show():
    st.title("Manual Student Entry")

    mid1 = st.number_input("Mid Sem 1",min_value=0,max_value=80,value=40)
    mid2 = st.number_input("Mid Sem 2",min_value=0,max_value=80,value=40)

    sgpa = st.number_input("Previous SGPA",min_value=0.0,max_value=10.0,value=5.0,step=0.01)

    cgpa = st.number_input("Current CGPA",min_value=0.0,max_value=10.0,value=5.0,step=0.01)

    hours = st.slider("Study Hours",0,18,4,1)

    os_m = st.number_input("OS Marks",min_value=0,max_value=100,value=33)

    cd_m = st.number_input("Compiler Design Marks",min_value=0,max_value=100,value=33)

    ml_m = st.number_input("Machine Learning Marks",min_value=0,max_value=100,value=33)

    sd_m = st.number_input("System Design Marks",min_value=0,max_value=100,value=33)

    if st.button("Predict"):

        final_marks = predict_marks([
            mid1,
            mid2,
            sgpa,
            cgpa,
            hours,
            os_m,
            cd_m,
            ml_m,
            sd_m
        ])

        strong, weak = subject_analysis(
            os_m,
            cd_m,
            ml_m,
            sd_m
        )

        st.success(
            f"Predicted Final Marks: {final_marks}"
        )

        st.info(
            f"Strong Subject: {strong}"
        )

        st.warning(
            f"Need More Practice: {weak}"
        )
        
            
            


        fig = subject_plot(
                os_m,
                cd_m,
                ml_m,
                sd_m
            )

        st.pyplot(fig)