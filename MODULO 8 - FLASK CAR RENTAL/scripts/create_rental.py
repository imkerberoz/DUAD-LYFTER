#This is a script to create a rental in the database. It checks if the car is available, creates the rental, and updates the car's status to "rented". It uses psycopg2 to connect to a PostgreSQL database and dotenv to load environment variables for database connection parameters.
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

def create_rental(user_id, car_id):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # 1. We confirm if the car is available for rental. If the car is not available, we print a warning message and return early from the function.
        cur.execute("""
            SELECT status FROM lyfter_car_rental.cars WHERE id = %s;
        """, (car_id,))
        result = cur.fetchone()

        if not result:
            print(f"⚠️ No existe el automóvil con ID {car_id}")
            return

        if result[0] != "available":
            print(f"⚠️ El automóvil {car_id} no está disponible (estado: {result[0]})")
            return

        # 2. Crear el alquiler
        cur.execute("""
            INSERT INTO lyfter_car_rental.rentals (user_id, car_id, status)
            VALUES (%s, %s, 'active')
            RETURNING id;
        """, (user_id, car_id))

        rental_id = cur.fetchone()[0]

        # 3. Cambiar el estado del carro a "rented"
        cur.execute("""
            UPDATE lyfter_car_rental.cars
            SET status = 'rented'
            WHERE id = %s;
        """, (car_id,))

        conn.commit()
        print(f"✅ Alquiler creado correctamente. ID del alquiler: {rental_id}")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"❌ Error al crear alquiler: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # Ejemplo: usuario 1 alquila el carro 2
    create_rental(user_id=51, car_id=2)