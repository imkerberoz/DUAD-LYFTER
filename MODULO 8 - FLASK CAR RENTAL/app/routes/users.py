# User routes (endpoints).
# Before: Contained SQL queries and database connection logic.
# Now: Only handles HTTP request/response and calls user_repository.
# Also changed: /moroso → /delinquent (code must be in English).

from flask import Blueprint, request, jsonify
from app.repositories import user_repository

users_bp = Blueprint("users", __name__)

# ------------------------------------------------------
# POST /users  → Create a new user
# ------------------------------------------------------
@users_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    required_fields = ["name", "email", "username", "password", "birth_date"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        new_user = user_repository.create_user(
            name=data["name"],
            email=data["email"],
            username=data["username"],
            password=data["password"],
            birth_date=data["birth_date"],
            account_status=data.get("account_status", "active")
        )
        return jsonify(new_user), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------
# GET /users  → List users (with optional filters)
# ------------------------------------------------------
@users_bp.route("/users", methods=["GET"])
def get_users():
    try:
        filters = request.args
        users = user_repository.get_users(filters)
        return jsonify(users), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------
# PATCH /users/<id>/status  → Change user status
# ------------------------------------------------------
@users_bp.route("/users/<int:user_id>/status", methods=["PATCH"])
def change_user_status(user_id):
    data = request.get_json()

    if "account_status" not in data:
        return jsonify({"error": "Missing field: account_status"}), 400

    try:
        updated_user = user_repository.update_user_status(user_id, data["account_status"])

        if not updated_user:
            return jsonify({"error": "User not found"}), 404

        return jsonify(updated_user), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------
# PATCH /users/<id>/delinquent  → Flag user as delinquent
# ------------------------------------------------------
@users_bp.route("/users/<int:user_id>/delinquent", methods=["PATCH"])
def flag_user_as_delinquent(user_id):
    try:
        updated_user = user_repository.flag_user_as_delinquent(user_id)

        if not updated_user:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            **updated_user,
            "message": "User flagged as delinquent"
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500