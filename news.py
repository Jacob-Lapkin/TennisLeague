from newsapi import NewsApiClient
import datetime 
import os
from dotenv import load_dotenv

load_dotenv()

news_api = os.getenv("news_api_key")
# Init
newsapi = NewsApiClient(api_key=news_api)
all_articles = newsapi.get_everything(q='US Open',
                                      from_param='2022-08-01',
                                      language='en',
                                      sort_by='relevancy',
                                      page=1)


def get_kyrgios_news():
    # /v2/everything
    only_articles = all_articles['articles']
    return only_articles

print(get_kyrgios_news())