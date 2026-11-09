# In a real world application, we would want to provide a way for users to see which cars are currently available for rental. This script provides a simple way to retrieve and display all cars that are marked as "available" in the database.
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

def get_available_cars():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, brand, model, year, status
            FROM lyfter_car_rental.cars
            WHERE status = 'available'
            ORDER BY id;
        """)

        rows = cur.fetchall()

        if not rows:
            print("ℹ️ No hay carros disponibles actualmente.")
        else:
            print(f"\n✅ Carros disponibles ({len(rows)}):\n")
            for row in rows:
                print(f"ID: {row[0]} | {row[1]} {row[2]} ({row[3]}) | Estado: {row[4]}")

    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    get_available_cars()