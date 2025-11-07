import psycopg2 as pg
from util.get_data_env import get_database_data

database_host, database_port, database_name_db, database_name_user, database_password = get_database_data()

conn = pg.connect(
    database=database_name_db,
    user=database_name_user,
    password=database_password,
    host=database_host,
    port=database_port
)