from newsapi import NewsApiClient
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

news_api = os.getenv("news_api_key")
# Init
if datetime.now().month != 1:
    year = datetime.now().year
    month = datetime.now().month - 1
if datetime.now().month == 1:
    year = datetime.now().year - 1
    month = 12
day = datetime.now().day
if day < 10 and month < 10:
    from_date = f'{year}-0{month}-0{day}'
elif day < 10:
    from_date = f'{year}-{month}-0{day}'
elif month < 10:
    from_date = f'{year}-0{month}-{day}'
else: 
        from_date = f'{year}-{month}-{day}'

newsapi = NewsApiClient(api_key=news_api)
all_articles = newsapi.get_everything(q='Kyrgios',
                                      from_param=from_date,
                                      language='en',
                                      sort_by='publishedAt',
                                      page=1)


def get_kyrgios_news():
    # /v2/everything
    only_articles = all_articles['articles']
    return only_articles


