import os
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

def create_schema_and_tables():
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()

        # 1. Crear el schema
        cur.execute("CREATE SCHEMA IF NOT EXISTS lyfter_car_rental;")
        print("✅ Schema 'lyfter_car_rental' creado (o ya existía).")

        # 2. Tabla de USERS
        cur.execute("""
            CREATE TABLE IF NOT EXISTS lyfter_car_rental.users (
                id              SERIAL PRIMARY KEY,
                name            VARCHAR(100) NOT NULL,
                email           VARCHAR(150) UNIQUE NOT NULL,
                username        VARCHAR(50) UNIQUE NOT NULL,
                password        VARCHAR(255) NOT NULL,
                birth_date      DATE NOT NULL,
                account_status  VARCHAR(20) NOT NULL DEFAULT 'active',
                created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        print("✅ Tabla 'users' creada.")

        # 3. Tabla de CARS
        cur.execute("""
            CREATE TABLE IF NOT EXISTS lyfter_car_rental.cars (
                id          SERIAL PRIMARY KEY,
                brand       VARCHAR(50) NOT NULL,
                model       VARCHAR(50) NOT NULL,
                year        INTEGER NOT NULL,
                status      VARCHAR(20) NOT NULL DEFAULT 'available',
                created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        print("✅ Tabla 'cars' creada.")

        # 4. Tabla de RENTALS (tabla cruz)
        cur.execute("""
            CREATE TABLE IF NOT EXISTS lyfter_car_rental.rentals (
                id           SERIAL PRIMARY KEY,
                user_id      INTEGER NOT NULL REFERENCES lyfter_car_rental.users(id),
                car_id       INTEGER NOT NULL REFERENCES lyfter_car_rental.cars(id),
                rental_date  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                status       VARCHAR(20) NOT NULL DEFAULT 'active',
                created_at   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        """)
        print("✅ Tabla 'rentals' creada.")

        conn.commit()
        print("\n🎉 Schema y tablas creadas exitosamente.")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"❌ Error al crear schema/tablas: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    create_schema_and_tables()