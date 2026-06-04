import pandas as pd
import pickle

from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("C:/Users/ASUS/Desktop/student_marks_prediction/data/student_dataset.csv")

X = df.drop("FinalMarks", axis=1)
y = df["FinalMarks"]

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X, y)

with open("student_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model Trained Successfully")