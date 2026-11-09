# This repository handles all database operations related to rentals.
# Before: SQL and business logic were inside the rentals routes.
# Improvements applied:
#   1. Validates that the user exists before creating a rental (avoids 500 error).
#   2. Validates that the car exists and is available.
#   3. Keeps car status synchronized with the rental status.
# Related to: app/routes/rentals.py

from app.database import get_connection

def create_rental(user_id, car_id):
    """
    Creates a new rental.
    Validates that both the user and the car exist,
    and that the car is available.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # 1. Check if the user exists
        cur.execute("""
            SELECT id FROM lyfter_car_rental.users WHERE id = %s;
        """, (user_id,))
        user = cur.fetchone()

        if not user:
            return {"error": "User not found", "status_code": 404}

        # 2. Check if the car exists and is available
        cur.execute("""
            SELECT status FROM lyfter_car_rental.cars WHERE id = %s;
        """, (car_id,))
        car = cur.fetchone()

        if not car:
            return {"error": "Car not found", "status_code": 404}

        if car[0] != "available":
            return {
                "error": f"Car is not available (current status: {car[0]})",
                "status_code": 400
            }

        # 3. Create the rental
        cur.execute("""
            INSERT INTO lyfter_car_rental.rentals (user_id, car_id, status)
            VALUES (%s, %s, 'active')
            RETURNING id, user_id, car_id, rental_date, status;
        """, (user_id, car_id))

        rental = cur.fetchone()

        # 4. Update car status to 'rented'
        cur.execute("""
            UPDATE lyfter_car_rental.cars
            SET status = 'rented'
            WHERE id = %s;
        """, (car_id,))

        conn.commit()

        return {
            "id": rental[0],
            "user_id": rental[1],
            "car_id": rental[2],
            "rental_date": str(rental[3]),
            "status": rental[4]
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

def get_rentals(filters=None):
    """
    Returns a list of rentals. Can receive optional filters.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        query = """
            SELECT id, user_id, car_id, rental_date, status 
            FROM lyfter_car_rental.rentals
        """
        values = []
        conditions = []

        allowed_columns = ["id", "user_id", "car_id", "status"]

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

        rentals = []
        for row in rows:
            rentals.append({
                "id": row[0],
                "user_id": row[1],
                "car_id": row[2],
                "rental_date": str(row[3]),
                "status": row[4]
            })

        return rentals

    except Exception as e:
        raise e
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

def complete_rental(rental_id):
    """
    Completes a rental and sets the car back to available.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # 1. Get the rental
        cur.execute("""
            SELECT car_id, status FROM lyfter_car_rental.rentals
            WHERE id = %s;
        """, (rental_id,))
        rental = cur.fetchone()

        if not rental:
            return {"error": "Rental not found", "status_code": 404}

        car_id, current_status = rental

        if current_status != "active":
            return {
                "error": f"Rental is not active (current status: {current_status})",
                "status_code": 400
            }

        # 2. Mark rental as completed
        cur.execute("""
            UPDATE lyfter_car_rental.rentals
            SET status = 'completed'
            WHERE id = %s;
        """, (rental_id,))

        # 3. Set car back to available
        cur.execute("""
            UPDATE lyfter_car_rental.cars
            SET status = 'available'
            WHERE id = %s;
        """, (car_id,))

        conn.commit()

        return {
            "message": "Rental completed successfully",
            "rental_id": rental_id,
            "car_id": car_id,
            "car_status": "available"
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

def update_rental_status(rental_id, new_status):
    """
    Updates the status of a rental.
    """
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE lyfter_car_rental.rentals
            SET status = %s
            WHERE id = %s
            RETURNING id, user_id, car_id, status;
        """, (new_status, rental_id))

        rental = cur.fetchone()

        if not rental:
            return None

        conn.commit()

        return {
            "id": rental[0],
            "user_id": rental[1],
            "car_id": rental[2],
            "status": rental[3]
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