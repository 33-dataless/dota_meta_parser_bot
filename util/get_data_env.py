import os

def get_stratz_api_env():
    stratz_api_env = os.getenv('STRATZ_API', 'get api from https://stratz.com/api, and add them in your environment variables')
    print('\nstratz_api_env: Ok')
    return stratz_api_env

def get_tg_bot_api_env():
    tb_bot_api = os.getenv('TG_BOT_TOKEN', 'get bot token in @BotFather, and add them in your environment variables')
    print('tg_bot_api: Ok')
    return tb_bot_api

def get_database_data():
    database_host = os.getenv('DATABASE_HOST', 'not found database host ( in env )')
    database_port = os.getenv('DATABASE_PORT', 'not found port database ( in env )')
    database_name_db = os.getenv('DATABASE_NAME_DB', 'not foudn name database ( in env )')
    database_name_user = os.getenv('DATABASE_NAME_USER', 'not found database name user ( in env )')
    database_password = os.getenv('DATABASE_PASSWORD', 'not found database password ( in env )')
    print('database value\'s: Ok')
    return database_host, database_port, database_name_db, database_name_user, database_password

