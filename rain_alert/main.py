import requests
from twilio.rest import Client

account_sid = "ACe86a551d2e90960564069efc514cd251"
auth_token = "e5b4fdd0d9851bdce6163c0e57adc763"

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"

api_key = "069c2703122b4294aee883bf88a671ce"
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





