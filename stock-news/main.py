# Imports
import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
load_dotenv()


# Global variables
STOCK_NAME = "BAESY"
COMPANY_NAME = "BAE Systems Plc"

# API Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "http://eventregistry.org/api/v1/article/getArticles"
NEWS_ENDPOINT2 = "https://api.newscatcherapi.com/v2/search"
# "https://newsapi.org/v2/everything"

# API Keys
API_KEY = os.getenv("ALPHAV_KEY")  # Alpha Vantage
NEWS_Key = os.getenv("NEWS_KEY")  # Event Registry
NEWS_KEY2 = os.getenv("NEWSCATCHER_KEY")

# Twilio
ACCOUNT_SID = os.getenv("TWILIO_SID")
AUTH_TOKEN = os.getenv("TWILIO_TOKEN")
USER_PHONE = "+447908669021"
TWILIO_PHONE = os.getenv("TWILIO_PHONE")

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily - Read docs
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
# Define parameters
parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "outputsize": "compact",
    "apikey": API_KEY
}
# API Call
response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
# Convert response to JSON
closing_data = response.json()
# Save only the daily time series as variable
time_series = closing_data['Time Series (Daily)']
# List comprehension to allow indexing
yesterday_series = [series for (date, series) in time_series.items()]

# Get 'yesterday' by calling 0 index
yesterday_close = float(yesterday_series[0]['4. close'])
# Get day before yesterday by calling 1 index
day_before_close = float(yesterday_series[1]['4. close'])

# Hint: https://www.w3schools.com/python/ref_func_abs.asp
difference = yesterday_close - day_before_close
pos_difference = abs(yesterday_close-day_before_close)

if difference > 0:
    up_down = "⬆️"
else:
    up_down = "⬇️"

# Percentage difference can be found by dividing the absolute (positive) value of change between 2 value by the average#
# of those values multiplied by 100
average = (yesterday_close+day_before_close)/2
percentage_diff = round((pos_difference/average)*100)


# If TODO4 percentage is greater than 5 then print("Get News").
if percentage_diff > 5:
    printt("Get News")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

querystring = {"q":"\"BAE Systems Plc\"","to_rank":10000,"lang":"en","sort_by":"relevancy","page":"1"}

headers = {
    "x-api-key": NEWS_KEY2
}

news_response = requests.request("GET", url=NEWS_ENDPOINT2, headers=headers, params=querystring)
news_response.raise_for_status()
news_data = news_response.json()
news_slice = news_data['articles'][:3]
article_list = [(x['title'], x['excerpt'], x['link']) for x in news_slice]

client = Client(ACCOUNT_SID, AUTH_TOKEN)

for i in range(0, len(article_list)):
    title = (article_list[i][0])
    excerpt = (article_list[i][1])
    link = (article_list[i][2])
    message_body = f"""
    {STOCK_NAME}: {up_down} {percentage_diff}
    {title}
    
    {excerpt}
    
    {link}
    """
    message = client.messages.create(
        to=USER_PHONE,
        from_=TWILIO_PHONE,
        body=message_body
    )
    print(message.sid)

# news_parameters = {
#     "action": "getArticles",
#     "keyword": "BAE Systems Plc",
#     "articlesPage": 1,
#     "articlesCount": 5,
#     "articlesSortBy": "date",
#     "articlesSortByAsc": False,
#     "articlesArticleBodyLen": 500,
#     "resultType": "articles",
#     "dataType": [
#         "news"
#     ],
#     "apiKey": NEWS_Key,
#     "forceMaxDataTimeWindow": 31
# }
#
# news_response = requests.get(NEWS_ENDPOINT, news_parameters)
# news_response.raise_for_status()
# news_data = news_response.json()
# #Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
# news_slice = news_data['articles']['results'][:3]
#     ## STEP 3: Use twilio.com/docs/sms/quickstart/python
#     #to send a separate message with each article's title and description to your phone number.
# article_list = [(x['title'], x['body']) for x in news_slice]



#  - Send each article as a separate message via Twilio.

#Optional  Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""






