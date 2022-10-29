import requests
import os
from dotenv import load_dotenv
load_dotenv()
# Global Variables
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

# Pixela signup - comment out after first run
user_params = {
    "token": "hgt567tgsy32",
    "username": "cjpar",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
response.raise_for_status()






