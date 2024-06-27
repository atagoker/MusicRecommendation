import os

class Config:
    SPOTIFY_API_TOKEN = os.getenv('SPOTIFY_API_TOKEN')
    DATABASE_URL = os.getenv('DATABASE_URL')
