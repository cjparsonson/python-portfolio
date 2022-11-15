import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()
account_sid = os.getenv("TWILIOSID")
auth_token = os.getenv("TWILIOTOKEN")

OWM_Endpoint = os.getenv("OWMENDPOINT")

api_key = os.getenv("OWMKEY")
LAT = 50.909698
LON = -1.404351

weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "exclude": "current,minutely,daily",
    "units": "metric",
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()

will_rain = False
hour_list = weather_data['hourly'][:12]

for hour in hour_list:
    condition_code = hour["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    Message_body = "Rain expected today ☔"
else:
    weather_main = hour_list[0]["weather"][0]["main"]
    Message_body = f"Main weather state today: {weather_main}"

# Declare Twilio client
client = Client(account_sid, auth_token)
message = client.messages \
                .create(
                     body=Message_body,
                     from_="+18085635718",
                     to="+447908669021"
                 )

print(message.status)





