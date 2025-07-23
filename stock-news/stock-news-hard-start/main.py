import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = '5NISYBP8EVY643BZ'
NEWS_API_KEY = '504307d694094dd698d1c79de4eb23d9'

yesterday = datetime.now().date() - timedelta(days=1)
day_before = yesterday - timedelta(days=1)
lastmonth = yesterday - timedelta(days=30)

def stock_difference():
    stock_parameters = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK,
        'interval':'5min',
        'apikey': STOCK_API_KEY
    }

    response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
    response.raise_for_status()
    print(response.json())
    data = response.json()['Time Series (Daily)']

    init_value = float(data[str(day_before)]['4. close'])
    fin_value = float(data[str(yesterday)]['4. close'])
    stock_diff = abs(fin_value - init_value) / fin_value * 100

    if fin_value - init_value < 0:
        direction = '🔻'
    else:
        direction = '🔺'

    if not stock_diff >= 5:
        print('get news')
        return True, stock_diff, direction


def get_news(diff, direction):
    news_parameters = {
        'q': COMPANY_NAME,
        'from': lastmonth,
        'sortby': 'publishedAt',
        'language': 'en',
        'apikey': NEWS_API_KEY,
    }

    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    response.raise_for_status()
    articles = response.json()['articles'][:3]
    print(response.json())
    print(articles)
    print(f'{STOCK}: {direction}{diff}%')
    for article in articles:
        headline = article['title']
        brief = article['description']
        print(f'Headline: {headline}\nBrief: {brief}\n\n')


#isTrue, diff, direction = stock_difference()
isTrue, diff, direction = True, 5, '🔺'
if isTrue:
    get_news(diff, direction)



from http.client import responses

from pandas.core.tools.times import to_time

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price.



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME.
#HINT 1: Think about using the Python Slice Operator



## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number.
#HINT 1: Consider using a List Comprehension.



#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


