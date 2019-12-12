from sqlalchemy.dialects.postgresql import psycopg2

POSTGRE_USERNAME = "vnas_quantri"
POSTGRE_PASSWORD = "asdad!my_4_vnas_678"
POSTGRE_HOSTNAME = "171.244.51.228"
POSTGRE_PORT = 8182
POSTGRE_DATABASE_NAME = "hvcngao"

POSTGRES_CONNECTION_STR = "postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}".format(
    DB_USER=POSTGRE_USERNAME,
    DB_PASS=POSTGRE_PASSWORD,
    DB_HOST=POSTGRE_HOSTNAME,
    DB_PORT=POSTGRE_PORT,
    DB_NAME=POSTGRE_DATABASE_NAME
)

def postgre_connection():
    connection = psycopg2.connect(user=POSTGRE_USERNAME, password=POSTGRE_PASSWORD, host=POSTGRE_HOSTNAME,
                                  port=POSTGRE_PORT,
                                  database=POSTGRE_DATABASE_NAME)
    return connection