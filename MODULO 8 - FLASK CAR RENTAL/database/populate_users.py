# This script creates the users table AND populates it in a single execution.
# Before: Table creation was in create_schema_and_tables.py and population was separate.
# Now: Meets the requirement of creating + populating with one script run.

import os
import random
from datetime import date, timedelta
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

FIRST_NAMES = [
    "Carlos", "Maria", "Jose", "Ana", "Luis", "Sofia", "Miguel", "Laura", "Diego", "Valentina",
    "Andres", "Camila", "Juan", "Isabella", "Pedro", "Lucia", "Fernando", "Paula", "Ricardo", "Daniela",
    "Jorge", "Gabriela", "Alejandro", "Mariana", "Roberto", "Natalia", "Eduardo", "Andrea", "Hector", "Carolina"
]

LAST_NAMES = [
    "Garcia", "Rodriguez", "Martinez", "Lopez", "Gonzalez", "Hernandez", "Perez", "Sanchez", "Ramirez", "Torres",
    "Flores", "Rivera", "Gomez", "Diaz", "Reyes", "Morales", "Cruz", "Ortiz", "Ramos", "Vargas"
]

STATUSES = ["active", "active", "active", "inactive", "suspended"]

def random_birth_date():
    start = date(1970, 1, 1)
    end = date(2005, 12, 31)
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def create_and_populate_users(n=50):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # 1. Create schema if it does not exist
        cur.execute("CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;")

        # 2. Create users table if it does not exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS lyfter_car_rental.users (
                id              SERIAL PRIMARY KEY,
                name            VARCHAR(100) NOT NULL,
                email           VARCHAR(150) UNIQUE NOT NULL,
                username        VARCHAR(50) UNIQUE NOT NULL,
                password        VARCHAR(255) NOT NULL,
                birth_date      DATE NOT NULL,
                account_status  VARCHAR(20) NOT NULL DEFAULT 'active',
                created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        print("Users table created (or already existed).")

        # 3. Populate the table
        inserted = 0
        for i in range(1, n + 1):
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            name = f"{first} {last}"
            email = f"{first.lower()}.{last.lower()}{i}@example.com"
            username = f"{first.lower()}{last.lower()}{i}"
            password = f"pass{i}123"
            birth_date = random_birth_date()
            status = random.choice(STATUSES)

            cur.execute("""
                INSERT INTO lyfter_car_rental.users
                    (name, email, username, password, birth_date, account_status)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (email) DO NOTHING;
            """, (name, email, username, password, birth_date, status))

            if cur.rowcount > 0:
                inserted += 1

        conn.commit()
        print(f"{inserted} users inserted successfully.")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    create_and_populate_users(50)