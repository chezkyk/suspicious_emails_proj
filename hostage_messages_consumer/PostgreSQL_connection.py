import psycopg2
from flask_sqlalchemy import SQLAlchemy

db_postgres = SQLAlchemy()

def check_db_connection():
    try:
        conn = psycopg2.connect(
            dbname='suspicious_hostage_content',
            user='postgres',
            password='1234',
            host='localhost',
            port='5432'
        )
        conn.close()
        print("Connection to database is successful.")
    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
        exit(1)