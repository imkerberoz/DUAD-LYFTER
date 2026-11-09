import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env

def get_connection():
    # Crea la conexión a PostgreSQL using the data from the .env file
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

def add_user(name, email, username, password, birth_date, account_status="active"):
    conn = None
    cur = None
    try:
        conn = get_connection() #this line establishes a connection to the database using the get_connection function defined above.
        cur = conn.cursor() #this line creates a cursor object that allows SQL to run commands in the database.

        # Inserta un nuevo usuario en la tabla
        cur.execute("""
            INSERT INTO lyfter_car_rental.users 
                (name, email, username, password, birth_date, account_status)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id;
        """, (name, email, username, password, birth_date, account_status))

        new_id = cur.fetchone()[0]  # Gets the ID of the newly inserted user, the "()" around the SQL query allows for parameterized queries, which helps prevent SQL injection attacks.And the "[]" is used to access the first element of the tuple returned by fetchone(), which is the ID of the newly inserted user.
        conn.commit()  # Guarda los cambios (Important to commit the transaction to make sure the changes are saved in the database)
        print(f"✅ Usuario creado correctamente con ID: {new_id}")

    except Exception as e:
        if conn:
            conn.rollback()  # Deshace cambios si hay error
        print(f"❌ Error al agregar usuario: {e}")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    # hERE we are calling the add_user function with sample data. This can be modified or removed as needed.
    add_user(
        name="Andrea Campos",
        email="andrea.campos@example.com",
        username="andreacampos",
        password="clave123",
        birth_date="1995-08-14"
    )