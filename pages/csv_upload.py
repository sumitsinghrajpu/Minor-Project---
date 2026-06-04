import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils.prediction import predict_marks

def show():

    st.title("CSV Upload")

    file = st.file_uploader(
        "Upload CSV",
        type=["csv"]
    )

    if file:

        df = pd.read_csv(file)

        predictions = []

        for _, row in df.iterrows():

            pred = predict_marks(
                row.values
            )

            predictions.append(pred)

        df["Predicted_Final"] = predictions

        st.dataframe(df)
        if st.button("Generate Visualization"):
            # fig,axes=plt.subplots(1,2,figsize=(10,4))
            fig=plt.figure(figsize=(10,4))
            st.write("figure created")
            plt.subplot(1,2,1)
            plt.bar(df['StudyHours'],df['Predicted_Final'])
            # plt.grid()
            plt.xlabel("StudyHours")
            plt.ylabel("Predicted_Final")
            plt.title("Empact of study hours")
            # axes[0][0].grid()
            plt.subplot(1,2,2)
            plt.scatter(df['CGPA'],df['Predicted_Final'])
            plt.grid()
            
            
            plt.ylabel("Predicted_Final")
            plt.title("cgpa__")
            # plt.grid()
            plt.tight_layout()
            st.pyplot(fig)
            

        st.download_button(
            "Download Results",
            df.to_csv(index=False),
            "prediction.csv"
        )
