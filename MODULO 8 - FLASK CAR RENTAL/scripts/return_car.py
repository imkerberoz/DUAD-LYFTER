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

def return_car(rental_id):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # 1. Obtener el car_id del alquiler
        cur.execute("""
            SELECT car_id, status FROM lyfter_car_rental.rentals
            WHERE id = %s;
        """, (rental_id,))
        result = cur.fetchone()
# The following ifs check if the rental exists and if its status is "active". If the rental does not exist, it prints a warning message. If the rental exists but is not active, it also prints a warning message. In both cases, the function returns early without making any changes to the database.
        if not result:
            print(f"⚠️ No existe el alquiler con ID {rental_id}")
            return

        car_id, current_status = result

        if current_status != "active":
            print(f"⚠️ El alquiler {rental_id} no está activo (estado: {current_status})")
            return

        # 2. Here we update the rental's status to 'completed' in the rentals table. This indicates that the rental has been successfully returned and is no longer active. The SQL UPDATE statement is executed with parameterized queries to ensure security and prevent SQL injection attacks. The rental_id is passed as a parameter to identify which rental record to update.
        cur.execute("""
            UPDATE lyfter_car_rental.rentals
            SET status = 'completed'
            WHERE id = %s;
        """, (rental_id,))

        # 3. In a life-like scenario, we would also want to update the status of the car back to 'available' in the cars table. This indicates that the car is now free for future rentals. The SQL UPDATE statement is executed with parameterized queries to ensure security and prevent SQL injection attacks. The car_id obtained from the previous query is passed as a parameter to identify which car record to update.
        cur.execute("""
            UPDATE lyfter_car_rental.cars
            SET status = 'available'
            WHERE id = %s;
        """, (car_id,))

        conn.commit()
        print(f"✅ Alquiler {rental_id} completado. Automóvil {car_id} ahora está disponible.")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"❌ Error al devolver el automóvil: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # Ejemplo: devolver el alquiler con ID 1
    return_car(rental_id=1)