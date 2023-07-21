import json
import requests

url = 'http://127.0.0.1:8000/diabetes_prediction'

input_data_for_model = {

    'Pregnancies': 9,
    'Glucose': 171,
    'BloodPressure': 110,
    'SkinThickness': 24,
    'Insulin': 240,
    'BMI': 45.4,
    'DiabetesPedigreeFunction': 0.721,
    'Age': 54

}

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)
