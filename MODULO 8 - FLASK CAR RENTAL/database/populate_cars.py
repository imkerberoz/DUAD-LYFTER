import os
import random
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

# Marcas y modelos reales (DUMMY LISTS)
BRANDS_MODELS = {
    "Toyota": ["Corolla", "Camry", "RAV4", "Hilux", "Yaris"],
    "Honda": ["Civic", "Accord", "CR-V", "HR-V", "Fit"],
    "Hyundai": ["Elantra", "Tucson", "Santa Fe", "Accent", "Kona"],
    "Kia": ["Rio", "Sportage", "Sorento", "Cerato", "Seltos"],
    "Nissan": ["Sentra", "Altima", "X-Trail", "Versa", "Frontier"],
    "Mazda": ["Mazda3", "CX-5", "CX-30", "Mazda6"],
    "Ford": ["Focus", "Escape", "Explorer", "Ranger"],
    "Chevrolet": ["Spark", "Onix", "Tracker", "Captiva"],
    "Volkswagen": ["Golf", "Jetta", "Tiguan", "Polo"],
    "Suzuki": ["Swift", "Vitara", "Jimny", "Baleno"]
}

STATUSES = ["available", "available", "available", "rented", "maintenance"]

def populate_cars(n=50):
    conn = None
    cur = None

    try:
        conn = get_connection()
        cur = conn.cursor()

        for _ in range(n):
            brand = random.choice(list(BRANDS_MODELS.keys()))
            model = random.choice(BRANDS_MODELS[brand])
            year = random.randint(2015, 2025)
            status = random.choice(STATUSES)

            cur.execute("""
                INSERT INTO lyfter_car_rental.cars (brand, model, year, status)
                VALUES (%s, %s, %s, %s);
            """, (brand, model, year, status))

        conn.commit()
        print(f"✅ {n} automóviles insertados correctamente.")

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"❌ Error al poblar automóviles: {e}")

    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

if __name__ == "__main__":
    populate_cars(50)