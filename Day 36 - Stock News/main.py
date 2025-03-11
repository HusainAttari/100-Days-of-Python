import requests
import smtplib
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_URL = 'https://www.alphavantage.co/query'
NEWS_URL = 'https://newsapi.org/v2/everything'
STOCK_API_KEY = os.environ['STOCK_API_KEY']
NEWS_API_KEY = os.environ['NEWS_API_KEY']
GMAIL_PASSWORD = os.environ['GMAIL_PASS']
GMAIL_ID = os.environ['GMAIL_ID']

stock_parameters = {
	'function': 'TIME_SERIES_DAILY',
	'symbol': STOCK,
	'apikey': STOCK_API_KEY,
}

news_parameters = {
	'apiKey': NEWS_API_KEY,
	'q': COMPANY_NAME,
	'searchIn': 'title',
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(STOCK_URL, params=stock_parameters)
response.raise_for_status()
data = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in data.items()]

yesterday_closing_point = float(data_list[0]['4. close'])
day_before_yesterday_closing_point = float(data_list[1]['4. close'])
difference = yesterday_closing_point - day_before_yesterday_closing_point
diff_percent = difference / yesterday_closing_point * 100

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

if abs(diff_percent) > 0 :
	r = requests.get(NEWS_URL, news_parameters)
	r.raise_for_status()
	article_list = r.json()['articles']
	articles = article_list[:3]

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(GMAIL_ID, GMAIL_PASSWORD)
message = f"{STOCK}: {f'🔺{round(abs(diff_percent))}' if diff_percent > 0 else f'🔻{round(abs(diff_percent))}'}\nHeadline: {articles[0]['title']}\nBrief: {articles[0]['description']}\nLink: [Click here to redirect to the article]({articles[0]['url']})".encode('utf8')
s.sendmail(GMAIL_ID, GMAIL_ID, message)
s.quit()
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

