import pickle

import numpy as np

with open("model/student_model.pkl", "rb") as f:
    model = pickle.load(f)

def predict_marks(data):

    data = np.array(data).reshape(1, -1)

    prediction = model.predict(data)

    return round(prediction[0], 2)/10