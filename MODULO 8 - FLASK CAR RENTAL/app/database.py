import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env

def get_connection():
    """
    Here we are defining a function called get_connection that establishes a connection to a PostgreSQL database using the psycopg2 library. The connection parameters (database name, user, password, host, and port) are retrieved from environment variables loaded from a .env file. This approach enhances security by keeping sensitive information out of the source code.
    """
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )