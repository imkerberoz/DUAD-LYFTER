# SUMMARY: THIS ONE IS DIVIDED INTO 4 PARTS: 
# 1) POST /users → Creating a new user, 
# 2) GET /users → Here we list all users, with optional filtering by query parameters, 
# 3) PATCH /users/<id>/status → CHANGE USER STATUS, 
# 4) PATCH /users/<id>/moroso → HERE WE MARK A USER AS "MOROSO" (DELINQUENT)

from flask import Blueprint, request, jsonify
from app.database import get_connection

# Creamos un Blueprint (grupo de rutas) para usuarios
users_bp = Blueprint("users", __name__)

# ------------------------------------------------------
# POST /users  → Creating a new user
# ------------------------------------------------------
@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    # Basic validation to ensure all required fields are present in the request data. If any required field is missing, we return a 400 Bad Request response with an error message indicating which field is missing. This helps ensure that the incoming request contains all necessary information before proceeding with database operations.
    required_fields = ["name", "email", "username", "password", "birth_date"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Falta el campo: {field}"}), 400

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO lyfter_car_rental.users 
                (name, email, username, password, birth_date, account_status)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id, name, email, username, birth_date, account_status;
        """, (
            data["name"],
            data["email"],
            data["username"],
            data["password"],
            data["birth_date"],
            data.get("account_status", "active")  # valor por defecto
        ))

        new_user = cur.fetchone()
        conn.commit()

        return jsonify({
            "id": new_user[0],
            "name": new_user[1],
            "email": new_user[2],
            "username": new_user[3],
            "birth_date": str(new_user[4]),
            "account_status": new_user[5]
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
# GET /users  → Here we list all users, with optional filtering by query parameters. The route retrieves all users from the database and allows filtering based on specific fields provided in the query string. This enables clients to fetch users based on criteria such as username, email, or account status.
# ------------------------------------------------------
@users_bp.route("/users", methods=["GET"])
def get_users():
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        # wE CATCH THE QUERY PARAMETERS FROM THE REQUEST. These parameters are used to filter the results based on specific criteria. For example, a client can request /users?username=andrea&account_status=active to retrieve users with the username "andrea" and an active account status.
        # EXAMPLE: /users?username=andrea&account_status=active
        filters = request.args
        query = "SELECT id, name, email, username, birth_date, account_status FROM lyfter_car_rental.users"
        values = []
        conditions = []

        # ALLOWED COLUMNS FOR FILTERING (SAFETY MEASURE). This list defines which columns can be used for filtering to prevent SQL injection and ensure that only valid fields are queried. Any query parameter not in this list will be ignored, enhancing security and maintaining the integrity of the database queries.
        allowed_columns = ["id", "name", "email", "username", "birth_date", "account_status"]

        for column, value in filters.items():
            if column in allowed_columns:
                conditions.append(f"{column} = %s")
                values.append(value)

        if conditions:
            query += " WHERE " + " AND ".join(conditions)

        query += " ORDER BY id"

        cur.execute(query, values)
        rows = cur.fetchall()

        users = []
        for row in rows:
            users.append({
                "id": row[0],
                "name": row[1],
                "email": row[2],
                "username": row[3],
                "birth_date": str(row[4]),
                "account_status": row[5]
            })

        return jsonify(users), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()

# ------------------------------------------------------
# PATCH /users/<id>/status  → CHANGE USER STATUS. This route allows updating the account status of a specific user identified by their user ID. The client sends a PATCH request with the new account status in the request body, and the server updates the corresponding record in the database. This is useful for managing user accounts, such as activating or deactivating them.
# ------------------------------------------------------
@users_bp.route("/users/<int:user_id>/status", methods=["PATCH"])
def change_user_status(user_id):
    data = request.get_json()

    if "account_status" not in data:
        return jsonify({"error": "Falta el campo: account_status"}), 400

    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE lyfter_car_rental.users
            SET account_status = %s
            WHERE id = %s
            RETURNING id, name, account_status;
        """, (data["account_status"], user_id))

        updated = cur.fetchone()

        if not updated:
            return jsonify({"error": "Usuario no encontrado"}), 404

        conn.commit()

        return jsonify({
            "id": updated[0],
            "name": updated[1],
            "account_status": updated[2]
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
# PATCH /users/<id>/moroso  → HERE WE MARK A USER AS "MOROSO" (DELINQUENT). This route allows updating the account status of a specific user to "moroso", indicating that the user has overdue payments or is in default. The client sends a
# ------------------------------------------------------
@users_bp.route("/users/<int:user_id>/moroso", methods=["PATCH"])
def flag_user_as_moroso(user_id):
    conn = None
    cur = None
    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            UPDATE lyfter_car_rental.users
            SET account_status = 'moroso'
            WHERE id = %s
            RETURNING id, name, account_status;
        """, (user_id,))

        updated = cur.fetchone()

        if not updated:
            return jsonify({"error": "Usuario no encontrado"}), 404

        conn.commit()

        return jsonify({
            "id": updated[0],
            "name": updated[1],
            "account_status": updated[2],
            "message": "Usuario marcado como moroso"
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