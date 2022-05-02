import os

class Config:
    NEWS_API_KEY = '0073535237c848a4b315104bc21e536e'
    NEWS_API_SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    TOP_HEADLINES_API_URL = 'https://newsapi.org/v2/top-headlines?country=ke&apiKey={}'
    ARTICLES_API_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    CATEGORIES_API_URL = 'https://newsapi.org/v2/top-headlines?country=ke&category={}&apiKey={}'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}