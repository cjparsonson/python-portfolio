# Workout Tracker with Google Sheets and Nutritionix API

# Imports
import os
import datetime
import requests
from dotenv import load_dotenv
load_dotenv()

# Globals
HEADERS = {
    "x-app-id": os.getenv('APP_ID'),
    "x-app-key": os.getenv('API_KEY')
}

GENDER = "male"
WEIGHT_KG = 82.55
HEIGHT_CM = 185.42
AGE = 35
DATETIME_TODAY = datetime.datetime.now()
DATE = DATETIME_TODAY.strftime("%d/%m/%Y")
TIME = DATETIME_TODAY.strftime("%H:%M:%S")

# Define endpoint
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_GET = os.getenv('GET_ENDPOINT')
SHEETY_POST = os.getenv('POST_ENDPOINT')


# Get Exercise Query
exercise_query = input("Tell me what exercise you did: ")
# Define params
params = {
    "query": exercise_query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=EXERCISE_ENDPOINT, json=params, headers=HEADERS)
response.raise_for_status()
result = response.json()


# Get data from JSON
exercise_name = result['exercises'][0]['name']
exercise_duration = result['exercises'][0]['duration_min']
exercise_calories = result['exercises'][0]['nf_calories']


# Build params
exercise_params = {
    "workout": {
        "date": DATE,
        "time": TIME,
        "exercise": exercise_name,
        "duration": exercise_duration,
        "calories": exercise_calories
    }
}

# Post row - Sheety needs the params sent as a json
response_sheety = requests.post(url=SHEETY_POST, json=exercise_params)
response_sheety.raise_for_status()
print(response_sheety)

