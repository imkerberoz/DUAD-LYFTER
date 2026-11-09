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

def get_rented_cars():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # This SQL query retrieves all cars that are currently rented from the database. It selects the car's ID, brand, model, year, and status from the "cars" table where the status is 'rented'. The results are ordered by the car's ID for better readability.
        cur.execute("""
            SELECT id, brand, model, year, status
            FROM lyfter_car_rental.cars
            WHERE status = 'rented'
            ORDER BY id;
        """)

        rows = cur.fetchall() #here the rows variable will contain a list of tuples, where each tuple represents a rented car's details (ID, brand, model, year, and status) retrieved from the database. If there are no rented cars, rows will be an empty list.

        if not rows:
            print("ℹ️ No hay automóviles alquilados actualmente.")
        else:
            print(f"\n🚗 Automóviles alquilados ({len(rows)}):\n")
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
    get_rented_cars()