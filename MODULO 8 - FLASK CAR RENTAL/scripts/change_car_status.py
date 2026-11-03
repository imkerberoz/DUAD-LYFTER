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

def change_car_status(car_id, new_status):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE lyfter_car_rental.cars
            SET status = %s
            WHERE id = %s;
        """, (new_status, car_id))

        if cur.rowcount == 0: # checks if any rows were affected by the update. If no rows were affected, it means that no car with the given ID was found in the database.
            print(f"⚠️ No se encontró automóvil con ID {car_id}")
        else:
            conn.commit()
            print(f"✅ Estado del automóvil {car_id} cambiado a '{new_status}'")

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
    change_car_status(car_id=1, new_status="maintenance")