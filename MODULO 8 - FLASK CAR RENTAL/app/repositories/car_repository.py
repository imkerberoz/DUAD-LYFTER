# This repository handles all database operations related to cars.
# Before: SQL was mixed inside the cars routes.
# Now: All INSERT, SELECT and UPDATE logic lives here.
# Related to: app/routes/cars.py (the route calls these functions).

from app.database import get_connection

def create_car(brand, model, year, status="available"):
    """
    Inserts a new car into the database and returns the created car.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO lyfter_car_rental.cars (brand, model, year, status)
            VALUES (%s, %s, %s, %s)
            RETURNING id, brand, model, year, status;
        """, (brand, model, year, status))

        car = cur.fetchone()
        conn.commit()

        return {
            "id": car[0],
            "brand": car[1],
            "model": car[2],
            "year": car[3],
            "status": car[4]
        }

    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def get_cars(filters=None):
    """
    Returns a list of cars. Can receive optional filters.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = "SELECT id, brand, model, year, status FROM lyfter_car_rental.cars"
        values = []
        conditions = []

        allowed_columns = ["id", "brand", "model", "year", "status"]

        if filters:
            for column, value in filters.items():
                if column in allowed_columns:
                    conditions.append(f"{column} = %s")
                    values.append(value)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " ORDER BY id"

        cur.execute(query, values)
        rows = cur.fetchall()

        cars = []
        for row in rows:
            cars.append({
                "id": row[0],
                "brand": row[1],
                "model": row[2],
                "year": row[3],
                "status": row[4]
            })

        return cars

    except Exception as e:
        raise e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def update_car_status(car_id, new_status):
    """
    Updates the status of a car.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE lyfter_car_rental.cars
            SET status = %s
            WHERE id = %s
            RETURNING id, brand, model, status;
        """, (new_status, car_id))

        car = cur.fetchone()

        if not car:
            return None

        conn.commit()

        return {
            "id": car[0],
            "brand": car[1],
            "model": car[2],
            "status": car[3]
        }

    except Exception as e:
        if conn:
            conn.rollback()
        raise e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()