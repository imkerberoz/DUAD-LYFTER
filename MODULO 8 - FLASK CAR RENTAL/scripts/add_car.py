import os
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

def add_car(brand, model, year, status="available"):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Inserts a new car into the table
        cur.execute("""
            INSERT INTO lyfter_car_rental.cars (brand, model, year, status)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """, (brand, model, year, status))

        new_id = cur.fetchone()[0] # Gets the ID of the newly inserted car.
        conn.commit()
        print(f"✅ Automóvil creado correctamente con ID: {new_id}")

    except Exception as e: # handles any exceptions that occur during the database operations. If an error occurs, it rolls back the transaction to maintain data integrity and prints an error message.
        if conn:
            conn.rollback()
        print(f"❌ Error al agregar automóvil: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    add_car(
        brand="Toyota",
        model="Corolla",
        year=2022
    )