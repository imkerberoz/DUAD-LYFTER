# In a real-world application, we would want to disable a car when it is no longer available for rental, 
# such as when it is being serviced or has been sold. This script provides a simple way to mark a car  as "disabled" 
# in the database, preventing it from being rented out until it is re-enabled.

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

def disable_car(car_id):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE lyfter_car_rental.cars
            SET status = 'disabled'
            WHERE id = %s; 
        """, (car_id,))

        if cur.rowcount == 0:
            print(f"⚠️ No se encontró automóvil con ID {car_id}")
        else:
            conn.commit()
            print(f"✅ Automóvil {car_id} deshabilitado correctamente.")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"❌ Error: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    disable_car(car_id=3)