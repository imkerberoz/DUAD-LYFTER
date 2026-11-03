import os
import random
from datetime import date, timedelta
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """Crea y retorna una conexión a la base de datos."""
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )

# DUMMY DATA LISTS
FIRST_NAMES = [
    "Carlos", "María", "José", "Ana", "Luis", "Sofía", "Miguel", "Laura", "Diego", "Valentina",
    "Andrés", "Camila", "Juan", "Isabella", "Pedro", "Lucía", "Fernando", "Paula", "Ricardo", "Daniela",
    "Jorge", "Gabriela", "Alejandro", "Mariana", "Roberto", "Natalia", "Eduardo", "Andrea", "Héctor", "Carolina"
]

LAST_NAMES = [
    "García", "Rodríguez", "Martínez", "López", "González", "Hernández", "Pérez", "Sánchez", "Ramírez", "Torres",
    "Flores", "Rivera", "Gómez", "Díaz", "Reyes", "Morales", "Cruz", "Ortiz", "Ramos", "Vargas"
]

STATUSES = ["active", "active", "active", "inactive", "suspended"]

def random_birth_date():
    """Genera una fecha de nacimiento aleatoria entre 1970 y 2005."""
    start = date(1970, 1, 1)
    end = date(2005, 12, 31)
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def populate_users(n=50):
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()

        inserted = 0

        for i in range(1, n + 1):
            first = random.choice(FIRST_NAMES)
            last = random.choice(LAST_NAMES)
            name = f"{first} {last}"
            email = f"{first.lower()}.{last.lower()}{i}@example.com"
            username = f"{first.lower()}{last.lower()}{i}"
            password = f"pass{i}123"
            birth_date = random_birth_date()
            status = random.choice(STATUSES)

            cur.execute("""
                INSERT INTO lyfter_car_rental.users
                    (name, email, username, password, birth_date, account_status)
                VALUES (%s, %s, %s, %s, %s, %s)
                ON CONFLICT (email) DO NOTHING;
            """, (name, email, username, password, birth_date, status))

            if cur.rowcount > 0:
                inserted += 1

        conn.commit()
        print(f"✅ {inserted} usuarios insertados correctamente.")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"❌ Error al poblar usuarios: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    populate_users(50)