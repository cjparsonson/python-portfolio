# Imports
import requests
import os
import datetime
from dotenv import load_dotenv
load_dotenv()


# Global variables
STOCK_NAME = "BAESY"
COMPANY_NAME = "BAE Systems Plc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "http://eventregistry.org/api/v1/article/getArticles"
# "https://newsapi.org/v2/everything"

API_KEY = os.getenv("ALPHAV_KEY")
NEWS_Key = os.getenv("NEWS_KEY")

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

#Hint: https://www.w3schools.com/python/ref_func_abs.asp
pos_difference = abs(yesterday_close-day_before_close)
print(yesterday_close)
print(day_before_close)
# Percentage difference can be found by dividing the absolute (positive) value of change between 2 value by the average#
# of those values multiplied by 100
average = (yesterday_close+day_before_close)/2
percentage_diff = (pos_difference/average)*100
print(percentage_diff)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if percentage_diff > 5:
    print("Get News")
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

news_parameters = {
    "action": "getArticles",
    "keyword": "BAE Systems Plc",
    "articlesPage": 1,
    "articlesCount": 5,
    "articlesSortBy": "date",
    "articlesSortByAsc": False,
    "articlesArticleBodyLen": -1,
    "resultType": "articles",
    "dataType": [
        "news"
    ],
    "apiKey": NEWS_Key,
    "forceMaxDataTimeWindow": 31
}

news_response = requests.get(NEWS_ENDPOINT, news_parameters)
news_response.raise_for_status()
news_data = news_response.json()

print(news_data)

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation

news_slice = news_data['articles']['results'][:3]
print(news_slice[0])
    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

