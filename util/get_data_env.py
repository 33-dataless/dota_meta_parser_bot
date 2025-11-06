import os

def get_data_env():
    return os.getenv('stratzApi', 'get api from https://stratz.com/api, and add them in your environment variables')

        