# Rental routes (endpoints).
# Before: Contained SQL and validation logic.
# Now: Only receives the request, calls rental_repository, and returns the response.
# Related to: app/repositories/rental_repository.py

from flask import Blueprint, request, jsonify
from app.repositories import rental_repository

rentals_bp = Blueprint("rentals", __name__)

# ------------------------------------------------------
# POST /rentals  → Create a new rental
# ------------------------------------------------------
@rentals_bp.route("/rentals", methods=["POST"])
def create_rental():
    data = request.get_json()

    if "user_id" not in data or "car_id" not in data:
        return jsonify({"error": "Missing fields: user_id and/or car_id"}), 400

    try:
        result = rental_repository.create_rental(data["user_id"], data["car_id"])

        # If the repository returned an error
        if "error" in result:
            return jsonify({"error": result["error"]}), result["status_code"]

        return jsonify(result), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------
# GET /rentals  → List rentals (with optional filters)
# ------------------------------------------------------
@rentals_bp.route("/rentals", methods=["GET"])
def get_rentals():
    try:
        filters = request.args
        rentals = rental_repository.get_rentals(filters)
        return jsonify(rentals), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------
# PATCH /rentals/<id>/complete  → Complete a rental
# ------------------------------------------------------
@rentals_bp.route("/rentals/<int:rental_id>/complete", methods=["PATCH"])
def complete_rental(rental_id):
    try:
        result = rental_repository.complete_rental(rental_id)

        if "error" in result:
            return jsonify({"error": result["error"]}), result["status_code"]

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------
# PATCH /rentals/<id>/status  → Change rental status
# ------------------------------------------------------
@rentals_bp.route("/rentals/<int:rental_id>/status", methods=["PATCH"])
def change_rental_status(rental_id):
    data = request.get_json()

    if "status" not in data:
        return jsonify({"error": "Missing field: status"}), 400

    try:
        updated_rental = rental_repository.update_rental_status(rental_id, data["status"])

        if not updated_rental:
            return jsonify({"error": "Rental not found"}), 404

        return jsonify(updated_rental), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500