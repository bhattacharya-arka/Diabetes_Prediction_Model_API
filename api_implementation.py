import json
import requests

url = 'http://127.0.0.1:8000/diabetes_prediction'

input_data_for_model = {

    'Pregnancies': 7,
    'Glucose': 147,
    'BloodPressure': 86,
    'SkinThickness': 5,
    'Insulin': 120,
    'BMI': 45.6,
    'DiabetesPedigreeFunction': 0.851,
    'Age': 43

}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)
