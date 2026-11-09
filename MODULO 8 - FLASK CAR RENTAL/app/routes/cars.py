# Car routes (endpoints).
# Before: Contained SQL queries directly.
# Now: Delegates all database work to car_repository.
# Related to: app/repositories/car_repository.py

from flask import Blueprint, request, jsonify
from app.repositories import car_repository

cars_bp = Blueprint("cars", __name__)

# ------------------------------------------------------
# POST /cars  → Create a new car
# ------------------------------------------------------
@cars_bp.route("/cars", methods=["POST"])
def create_car():
    data = request.get_json()

    required_fields = ["brand", "model", "year"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    try:
        new_car = car_repository.create_car(
            brand=data["brand"],
            model=data["model"],
            year=data["year"],
            status=data.get("status", "available")
        )
        return jsonify(new_car), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------
# GET /cars  → List cars (with optional filters)
# ------------------------------------------------------
@cars_bp.route("/cars", methods=["GET"])
def get_cars():
    try:
        filters = request.args
        cars = car_repository.get_cars(filters)
        return jsonify(cars), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ------------------------------------------------------
# PATCH /cars/<id>/status  → Change car status
# ------------------------------------------------------
@cars_bp.route("/cars/<int:car_id>/status", methods=["PATCH"])
def change_car_status(car_id):
    data = request.get_json()

    if "status" not in data:
        return jsonify({"error": "Missing field: status"}), 400

    try:
        updated_car = car_repository.update_car_status(car_id, data["status"])

        if not updated_car:
            return jsonify({"error": "Car not found"}), 404

        return jsonify(updated_car), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500