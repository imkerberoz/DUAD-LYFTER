# THIS ONE IS DIVIDED INTO FOUR PARTS:
# 1) POST /rentals → CREATING A NEW RENTAL, 
# 2) GET /rentals → TO CREATE A LIST OF RENTALS WITH OPTIONAL FILTERS,
# 3) PATCH /rentals/<id>/complete → THE RENTAL IS COMPLETED, THEREFORE, THE CAR IS RETURNED AND ITS STATUS IS CHANGED TO "AVAILABLE",
# 4) PATCH /rentals/<id>/status → WE CHANGE THE STATUS OF A SPECIFIC RENTAL. Each part is explained in detail below.

from flask import Blueprint, request, jsonify
from app.database import get_connection

# Blueprint FOR RENTALS
rentals_bp = Blueprint("rentals", __name__)

# ------------------------------------------------------
# POST /rentals  → CREATING A NEW RENTAL
# ------------------------------------------------------
@rentals_bp.route("/rentals", methods=["POST"])
def create_rental():
    data = request.get_json()

    if "user_id" not in data or "car_id" not in data:
        return jsonify({"error": "Faltan los campos user_id y/o car_id"}), 400

    user_id = data["user_id"]
    car_id = data["car_id"]

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # 1. hERE WE CHECK IF THE CAR IS AVAILABLE FOR RENTAL. If the car is not available, we return an error message indicating that the car is not available for rental.
        cur.execute("""
            SELECT status FROM lyfter_car_rental.cars WHERE id = %s;
        """, (car_id,))
        car = cur.fetchone()

        if not car:
            return jsonify({"error": "Automóvil no encontrado"}), 404

        if car[0] != "available":
            return jsonify({"error": f"El automóvil no está disponible (estado actual: {car[0]})"}), 400

        # 2. HERE WE CREATE THE RENTAL RECORD IN THE DATABASE. We insert a new record into the rentals table with the provided user_id and car_id, and set the status to 'active'. The RETURNING clause allows us to retrieve the newly created rental's details immediately after insertion.
        cur.execute("""
            INSERT INTO lyfter_car_rental.rentals (user_id, car_id, status)
            VALUES (%s, %s, 'active')
            RETURNING id, user_id, car_id, rental_date, status;
        """, (user_id, car_id))

        rental = cur.fetchone()

        # 3. HERE WE UPDATE THE STATUS OF THE CAR TO 'RENTED'. This ensures that the car is marked as rented in the database.
        cur.execute("""
            UPDATE lyfter_car_rental.cars
            SET status = 'rented'
            WHERE id = %s;
        """, (car_id,))

        conn.commit()

        return jsonify({
            "id": rental[0],
            "user_id": rental[1],
            "car_id": rental[2],
            "rental_date": str(rental[3]),
            "status": rental[4]
        }), 201

    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# ------------------------------------------------------
# GET /rentals  → TO CREATE A LIST OF RENTALS WITH OPTIONAL FILTERS. This route retrieves a list of rentals from the database, allowing clients to filter the results based on query parameters. The filters can include attributes like id, user_id, car_id, and status. The route constructs a dynamic SQL query based on the provided filters and returns the matching rentals in JSON format.
# ------------------------------------------------------
@rentals_bp.route("/rentals", methods=["GET"])
def get_rentals():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        filters = request.args
        query = """
            SELECT id, user_id, car_id, rental_date, status 
            FROM lyfter_car_rental.rentals
        """
        values = []
        conditions = []

        allowed_columns = ["id", "user_id", "car_id", "status"]

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

        return jsonify(rentals), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# ------------------------------------------------------
# PATCH /rentals/<id>/complete  → THE RENTAL IS COMPLETED, THEREFORE, THE CAR IS RETURNED AND ITS STATUS IS CHANGED TO "AVAILABLE". This route allows clients to mark a rental as completed. When a rental is completed, the status of the rental is updated to 'completed', and the status of the associated car is updated to 'available'. This ensures that the car can be rented again in the future.
# ------------------------------------------------------
@rentals_bp.route("/rentals/<int:rental_id>/complete", methods=["PATCH"])
def complete_rental(rental_id):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # 1. WE CHECK IF THE RENTAL EXISTS AND IF ITS STATUS IS "ACTIVE". If the rental does not exist, we return an error message indicating that the rental was not found. If the rental exists but is not active, we return an error message indicating that the rental is not active and cannot be completed.
        cur.execute("""
            SELECT car_id, status FROM lyfter_car_rental.rentals
            WHERE id = %s;
        """, (rental_id,))
        rental = cur.fetchone()

        if not rental:
            return jsonify({"error": "Alquiler no encontrado"}), 404

        car_id, current_status = rental

        if current_status != "active":
            return jsonify({"error": f"El alquiler no está activo (estado: {current_status})"}), 400

        # 2. THE RENTAL'S STATUS IS UPDATED TO 'COMPLETED' IN THE RENTALS TABLE. This indicates that the rental has been successfully completed and is no longer active. The SQL UPDATE statement is executed with parameterized queries to ensure security and prevent SQL injection attacks. The rental_id is passed as a parameter to identify which rental record to update.
        cur.execute("""
            UPDATE lyfter_car_rental.rentals
            SET status = 'completed'
            WHERE id = %s;
        """, (rental_id,))

        # 3. SINCE THE RENTAL IS COMPLETED, WE ALSO UPDATE THE STATUS OF THE CAR BACK TO 'AVAILABLE' IN THE CARS TABLE. This indicates that the car is now free for future rentals. The SQL UPDATE statement is executed with parameterized queries to ensure security and prevent SQL injection attacks. The car_id obtained from the previous query is passed as a parameter to identify which car record to update.
        cur.execute("""
            UPDATE lyfter_car_rental.cars
            SET status = 'available'
            WHERE id = %s;
        """, (car_id,))

        conn.commit()

        return jsonify({
            "message": "Alquiler completado correctamente",
            "rental_id": rental_id,
            "car_id": car_id,
            "car_status": "available"
        }), 200

    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# ------------------------------------------------------
# PATCH /rentals/<id>/status  → WE CHANGE THE STATUS OF A SPECIFIC RENTAL. This route allows clients to change the status of a rental identified by its ID. The new status is provided in the request body as JSON. The route updates the corresponding record in the database and returns the updated rental information in JSON format.
# ------------------------------------------------------
@rentals_bp.route("/rentals/<int:rental_id>/status", methods=["PATCH"])
def change_rental_status(rental_id):
    data = request.get_json()

    if "status" not in data:
        return jsonify({"error": "Falta el campo: status"}), 400

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
        """, (data["status"], rental_id))

        updated = cur.fetchone()

        if not updated:
            return jsonify({"error": "Alquiler no encontrado"}), 404

        conn.commit()

        return jsonify({
            "id": updated[0],
            "user_id": updated[1],
            "car_id": updated[2],
            "status": updated[3]
        }), 200

    except Exception as e:
        if conn:
            conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()