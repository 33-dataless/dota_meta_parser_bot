import os

def get_stratz_api_env():
    stratz_api_env = os.getenv('stratzApi', 'get api from https://stratz.com/api, and add them in your environment variables')
    print('stratz_api_env: Ok\n')
    return stratz_api_env

def get_tg_bot_api_env():
    tb_bot_api = os.getenv('tgBotApi', 'get bot token in @BotFather, and add them in your environment variables')
    print('tg_bot_api: Ok\n')
    return tb_bot_api


