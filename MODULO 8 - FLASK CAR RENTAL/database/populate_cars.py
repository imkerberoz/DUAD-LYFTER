# This script creates the cars table AND populates it in a single execution.
# Before: Table creation and population were split into different scripts.
# Now: Meets the requirement of creating + populating with one script run.

import os
import random
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

BRANDS_MODELS = {
    "Toyota": ["Corolla", "Camry", "RAV4", "Hilux", "Yaris"],
    "Honda": ["Civic", "Accord", "CR-V", "HR-V", "Fit"],
    "Hyundai": ["Elantra", "Tucson", "Santa Fe", "Accent", "Kona"],
    "Kia": ["Rio", "Sportage", "Sorento", "Cerato", "Seltos"],
    "Nissan": ["Sentra", "Altima", "X-Trail", "Versa", "Frontier"],
    "Mazda": ["Mazda3", "CX-5", "CX-30", "Mazda6"],
    "Ford": ["Focus", "Escape", "Explorer", "Ranger"],
    "Chevrolet": ["Spark", "Onix", "Tracker", "Captiva"],
    "Volkswagen": ["Golf", "Jetta", "Tiguan", "Polo"],
    "Suzuki": ["Swift", "Vitara", "Jimny", "Baleno"]
}

STATUSES = ["available", "available", "available", "rented", "maintenance"]

def create_and_populate_cars(n=50):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # 1. Create schema if it does not exist
        cur.execute("CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;")

        # 2. Create cars table if it does not exist
        cur.execute("""
            CREATE TABLE IF NOT EXISTS lyfter_car_rental.cars (
                id          SERIAL PRIMARY KEY,
                brand       VARCHAR(50) NOT NULL,
                model       VARCHAR(50) NOT NULL,
                year        INTEGER NOT NULL,
                status      VARCHAR(20) NOT NULL DEFAULT 'available',
                created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        print("Cars table created (or already existed).")

        # 3. Populate the table
        for _ in range(n):
            brand = random.choice(list(BRANDS_MODELS.keys()))
            model = random.choice(BRANDS_MODELS[brand])
            year = random.randint(2015, 2025)
            status = random.choice(STATUSES)

            cur.execute("""
                INSERT INTO lyfter_car_rental.cars (brand, model, year, status)
                VALUES (%s, %s, %s, %s);
            """, (brand, model, year, status))

        conn.commit()
        print(f"{n} cars inserted successfully.")

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
    create_and_populate_cars(50)