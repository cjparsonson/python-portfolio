import requests
import os
from dotenv import load_dotenv
load_dotenv()
# Global Variables
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/graph1"

# Pixela signup - comment out after first run
user_params = {
    "token": "hgt567tgsy32",
    "username": "cjpar",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# response.raise_for_status()
graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "Hour",
    "type": "float",
    "color": "momiji"
    }

pixel_post_params = {
    "date": "20221120",
    "quantity": "1"
}

headers = {
    "X-USER-TOKEN": os.getenv("PIXELA_TOKEN")
}
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)

response = requests.post(url=PIXEL_POST_ENDPOINT, json=pixel_post_params, headers=headers)
print(response.text)






