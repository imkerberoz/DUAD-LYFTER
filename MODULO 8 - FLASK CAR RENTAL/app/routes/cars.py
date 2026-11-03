# This one is divided into three parts: 
# 1. POST /cars → Creating a new car, 
# 2. GET /cars → Listing cars with optional filters, and 
# 3. PATCH /cars/<id>/status → Updating the status of a specific car. Each part is explained in detail below.

from flask import Blueprint, request, jsonify
from app.database import get_connection

# Blueprint para automóviles
cars_bp = Blueprint("cars", __name__)

# ------------------------------------------------------
# POST /cars  → Crating a new car
# ------------------------------------------------------
@cars_bp.route("/cars", methods=["POST"])
def create_car():
    data = request.get_json()

    required_fields = ["brand", "model", "year"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Falta el campo: {field}"}), 400

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO lyfter_car_rental.cars (brand, model, year, status)
            VALUES (%s, %s, %s, %s)
            RETURNING id, brand, model, year, status;
        """, (
            data["brand"],
            data["model"],
            data["year"],
            data.get("status", "available")
        ))

        new_car = cur.fetchone()
        conn.commit()

        return jsonify({
            "id": new_car[0],
            "brand": new_car[1],
            "model": new_car[2],
            "year": new_car[3],
            "status": new_car[4]
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
# GET /cars  → Listing cars with optional filters. This route retrieves a list of cars from the database, allowing clients to filter the results based on query parameters. The filters can include attributes like brand, model, year, and status. The route constructs a dynamic SQL query based on the provided filters and returns the matching cars in JSON format.
# ------------------------------------------------------
@cars_bp.route("/cars", methods=["GET"])
def get_cars():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        filters = request.args
        query = "SELECT id, brand, model, year, status FROM lyfter_car_rental.cars"
        values = []
        conditions = []

        # Here We eStablish a list of allowed columns that can be used for filtering. This is a security measure to prevent SQL injection and ensure that only valid columns are used in the query. The allowed_columns list includes the column names that are present in the cars table, such as id, brand, model, year, and status.
        allowed_columns = ["id", "brand", "model", "year", "status"]

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

        return jsonify(cars), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# ------------------------------------------------------
# PATCH /cars/<id>/status  → Updating the status of a specific car. This route allows clients to change the status of a car identified by its ID. The new status is provided in the request body as JSON. The route updates the corresponding record in the database and returns the updated car information in JSON format.
# ------------------------------------------------------
@cars_bp.route("/cars/<int:car_id>/status", methods=["PATCH"])
def change_car_status(car_id):
    data = request.get_json()

    if "status" not in data:
        return jsonify({"error": "Falta el campo: status"}), 400

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
        """, (data["status"], car_id))

        updated = cur.fetchone()

        if not updated:
            return jsonify({"error": "Automóvil no encontrado"}), 404

        conn.commit()

        return jsonify({
            "id": updated[0],
            "brand": updated[1],
            "model": updated[2],
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