from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
import numpy as np
from sklearn.preprocessing import StandardScaler

app = FastAPI()


class model_input(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


# loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))


@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    input_list = [preg, glu, bp, skin, insulin, bmi, dpf, age]

    input_data_as_np_array = np.asarray(input_list)
    input_data_reshaped = input_data_as_np_array.reshape(1, -1)
    scaler = StandardScaler()
    std_input_data = scaler.fit_transform(input_data_reshaped)

    prediction = diabetes_model.predict(std_input_data)

    if prediction[0] == 0:
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'
