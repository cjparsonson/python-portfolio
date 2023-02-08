import requests
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
load_dotenv()
# Global Variables
USERNAME = os.getenv("PIXELA_USERNAME")
TOKEN = os.getenv("PIXELA_TOKEN")
GRAPH_ID = "graph1"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
PIXEL_POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

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
    "id": GRAPH_ID,
    "name": "Programming Graph",
    "unit": "Hour",
    "type": "float",
    "color": "momiji"
    }

headers = {
    "X-USER-TOKEN": os.getenv("PIXELA_TOKEN")
}

today = datetime.now()
yesterday = datetime.now() - timedelta(1)
print(today.strftime("%Y%m%d"))
print(yesterday.strftime("%Y%m%d"))

pixel_post_params = {
    "date": yesterday.strftime("%Y%m%d"),
    "quantity": "1"
}


# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
# print(response.text)
#
# response = requests.post(url=PIXEL_POST_ENDPOINT, json=pixel_post_params, headers=headers)
# if "retry" in response.text:
#     response = requests.post(url=PIXEL_POST_ENDPOINT, json=pixel_post_params, headers=headers)

# Update Yesterday
# Get yesterday, format and create params
yesterday_formatted = yesterday.strftime("%Y%m%d")
pixel_update_params = {
    "quantity": "2"
}

# Build new endpoint
UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{yesterday_formatted}"

# Make PUT request
response = requests.put(url=UPDATE_ENDPOINT, json=pixel_update_params, headers=headers)
print(response.text)
if "retry" in response.text:
    response = requests.put(url=UPDATE_ENDPOINT, json=pixel_update_params, headers=headers)
    print(response.text)







