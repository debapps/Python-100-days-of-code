import os
from dotenv import load_dotenv
import requests
from twilio.rest import Client
from time import sleep

# STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday 
# then print("Get News").
# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and 
# description to your phone number. 


# Load the environment file into the program.
load_dotenv()

# Program Constants.
STOCK = input('\nEnter the stock id: ')
COMPANY_NAME = input('Enter the company name: ')

# STOCK = 'TSLA'
# COMPANY_NAME = 'Tesla Inc'
STOCK_TRADING_API_ENDPOINT = 'https://www.alphavantage.co/query'
STOCK_TRADING_PARAMS = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': os.getenv('STOCK_TRADE_API_KEY'),
}

NEWS_API_URL = 'https://newsapi.org/v2/everything'

ACCOUNT_SID = os.getenv('TWILIO_ACCNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TO_PHN_NUM = '+916290093829'

def call_api(url, params = {}):
    """This function returns the GET response of an API call."""
    response = requests.get(url=url, params=params)
    response.raise_for_status()

    data = response.json()
    return data

def get_news(comapny):
    """This function returns the latest relevant news abount the company"""

    NEWS_API_PARAMS = {
        'q': comapny,
        'searchIn': 'title',
        'sortBy': 'relevancy',
        'pageSize': 3,
        'language': 'en',
        'apikey': os.getenv('NEWS_API_KEY'),
    }
    news_api_data = call_api(url=NEWS_API_URL, params=NEWS_API_PARAMS)
    news_data = news_api_data['articles']
    news_data_content = [{
                          'title': news['title'], 
                          'description': news['description'], 
                          } for news in news_data]
    
    return news_data_content

def format_news_content(news_data, per_change):
    """This function format the news content and returns it."""

    if per_change > 0:
        change_symbol = '🔺'
    else:
        change_symbol = '🔻'
    
    company_news = []
    
    for news in news_data: 
        template_message = f'{STOCK} {change_symbol} {abs(per_change)}%\nHeadline: {news['title']}\nBrief: {news['description']}'
        company_news.append(template_message)

    return company_news


def send_sms(to_number, msg):
    """This function send SMS message provided to the phone number provided."""
    
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        from_=os.getenv('TWILIO_PHN_NUM'),
        body=msg,
        to=to_number
    )

    print(f'\nSMS is {message.status}')
    print('Messege Send - ')
    print(msg)


# Get the stock api data. 
stock_api_data = call_api(url=STOCK_TRADING_API_ENDPOINT, params=STOCK_TRADING_PARAMS)

# Format the stock data to get last 2 days closing price.
stock_daily_data = stock_api_data['Time Series (Daily)']
stock_close_data = [float(stock_daily_data[date]['4. close']) for date in stock_daily_data][:2]

# Get the percentage change in last 2 days closing price.
price_change = stock_close_data[0] - stock_close_data[1]
percentage_change = round(price_change / stock_close_data[0] * 100, 2)

# percentage_change = -8.27

# If the STOCK price increase/decreases by 5%, then get news.
if abs(percentage_change) > 5:
    # Get the news related to company. 
    company_news_data = get_news(COMPANY_NAME)

    # Format the news content.
    company_news = format_news_content(company_news_data, percentage_change)

    # For all the related company news, send the SMS.
    for news in company_news:
        sleep(10)
        send_sms(TO_PHN_NUM, news)
else: 
    print(f'\nThe percentage change for {STOCK}: {percentage_change}%')


