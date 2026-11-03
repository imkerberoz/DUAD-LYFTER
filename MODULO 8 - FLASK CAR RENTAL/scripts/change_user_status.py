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

def change_user_status(user_id, new_status):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # Method to change the status of a user in the database
        cur.execute("""
            UPDATE lyfter_car_rental.users
            SET account_status = %s 
            WHERE id = %s;
        """, (new_status, user_id)) # The above line executes an SQL UPDATE statement to change the account_status of a user in the users table. The %s placeholders are used for parameterized queries, which helps prevent SQL injection attacks. The new_status and user_id values are passed as a tuple to the execute method, ensuring that they are safely inserted into the query.

        if cur.rowcount == 0:
            print(f"⚠️ No se encontró usuario con ID {user_id}")
        else:
            conn.commit()
            print(f"✅ Estado del usuario {user_id} cambiado a '{new_status}'")

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
    # Here we call the change_user_status function with sample data. THis can be modified or removed as needed.
    change_user_status(user_id=1, new_status="suspended")