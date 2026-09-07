from flask import Flask, request, jsonify  # Import Flask, request object, and jsonify helper
import json  # Import json module to read/write the JSON file
import os  # Import os to check if the file exists

app = Flask(__name__)  # Create the Flask application instance

TASKS_FILE = "tasks.json"  # Name of the JSON file that will store the tasks
VALID_STATUSES = ["Por Hacer", "En Progreso", "Completada"]  # Allowed status values

def load_tasks():
    """Read all tasks from the JSON file. Return empty list if file does not exist or is empty."""
    if not os.path.exists(TASKS_FILE):  # Check if the file exists
        return []  # Return empty list if file is missing
    with open(TASKS_FILE, "r", encoding="utf-8") as f:  # Open the file in read mode
        content = f.read().strip()  # Read content and remove extra whitespace
        if not content:  # If the file is empty
            return []  # Return empty list
        return json.loads(content)  # Parse JSON and return the list of tasks

def save_tasks(tasks):
    """Write the list of tasks back to the JSON file."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:  # Open the file in write mode
        json.dump(tasks, f, indent=4, ensure_ascii=False)  # Write the list as pretty JSON

@app.route("/tasks", methods=["GET"])  # Endpoint to get all tasks (or filter by status)
def get_tasks():
    tasks = load_tasks()  # Load current tasks from file
    status = request.args.get("estado")  # Optional query parameter: ?estado=Por Hacer
    if status:  # If a status filter was provided
        if status not in VALID_STATUSES:  # Validate the status value
            return jsonify({"error": "Estado inválido"}), 400  # Return error if invalid
        tasks = [t for t in tasks if t["estado"] == status]  # Filter tasks by status
    return jsonify(tasks), 200  # Return the list of tasks

@app.route("/tasks", methods=["POST"])  # Endpoint to create a new task
def create_task():
    data = request.get_json()  # Get the JSON body from the request
    if not data:  # Check if body is missing
        return jsonify({"error": "No se envió ningún dato"}), 400

    # Required fields validation
    if "id" not in data:  # Check that id is present
        return jsonify({"error": "Falta el identificador"}), 400
    if "titulo" not in data or not data["titulo"]:  # Check that title is present and not empty
        return jsonify({"error": "El título es obligatorio"}), 400
    if "descripcion" not in data or not data["descripcion"]:  # Check that description is present and not empty
        return jsonify({"error": "La descripción es obligatoria"}), 400
    if "estado" not in data:  # Check that status is present
        return jsonify({"error": "El estado es obligatorio"}), 400
    if data["estado"] not in VALID_STATUSES:  # Check that status is one of the allowed values
        return jsonify({"error": "Estado inválido. Use: Por Hacer, En Progreso o Completada"}), 400

    tasks = load_tasks()  # Load existing tasks

    # Check for duplicate id
    if any(t["id"] == data["id"] for t in tasks):  # Look for an existing task with the same id
        return jsonify({"error": "Ya existe una tarea con ese identificador"}), 400

    # Create the new task object
    new_task = {
        "id": data["id"],  # Unique identifier
        "titulo": data["titulo"],  # Task title
        "descripcion": data["descripcion"],  # Task description
        "estado": data["estado"]  # Task status
    }

    tasks.append(new_task)  # Add the new task to the list
    save_tasks(tasks)  # Save the updated list to the file
    return jsonify(new_task), 201  # Return the created task with status 201

@app.route("/tasks/<task_id>", methods=["PUT"])  # Endpoint to update an existing task
def update_task(task_id):
    data = request.get_json()  # Get the JSON body
    if not data:  # Check if body is missing
        return jsonify({"error": "No se envió ningún dato"}), 400

    tasks = load_tasks()  # Load current tasks

    # Find the task by id
    task = next((t for t in tasks if t["id"] == task_id), None)  # Search for the task
    if not task:  # If not found
        return jsonify({"error": "Tarea no encontrada"}), 404

    # Update only the fields that were sent (and validate them)
    if "titulo" in data:
        if not data["titulo"]:  # Title cannot be empty
            return jsonify({"error": "El título no puede estar vacío"}), 400
        task["titulo"] = data["titulo"]  # Update title

    if "descripcion" in data:
        if not data["descripcion"]:  # Description cannot be empty
            return jsonify({"error": "La descripción no puede estar vacía"}), 400
        task["descripcion"] = data["descripcion"]  # Update description

    if "estado" in data:
        if data["estado"] not in VALID_STATUSES:  # Validate status
            return jsonify({"error": "Estado inválido"}), 400
        task["estado"] = data["estado"]  # Update status

    save_tasks(tasks)  # Save changes to the file
    return jsonify(task), 200  # Return the updated task

@app.route("/tasks/<task_id>", methods=["DELETE"])  # Endpoint to delete a task
def delete_task(task_id):
    tasks = load_tasks()  # Load current tasks
    original_length = len(tasks)  # Remember how many tasks we had

    # Keep only the tasks whose id is different from the one we want to delete
    tasks = [t for t in tasks if t["id"] != task_id]

    if len(tasks) == original_length:  # If the list length did not change, the task was not found
        return jsonify({"error": "Tarea no encontrada"}), 404

    save_tasks(tasks)  # Save the new list (without the deleted task)
    return jsonify({"message": "Tarea eliminada"}), 200  # Confirm deletion

if __name__ == "__main__":  # This block runs only when you execute the file directly
    app.run(debug=True)  # Start the development server with debug mode enabled