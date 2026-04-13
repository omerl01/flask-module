from flask import Flask, request, jsonify
from datetime import datetime, timezone
import uuid
app = Flask(__name__)

tasks = []
task1 = {
    "id":  str(uuid.uuid4()),
    "title": "Learn Flask",
    "completed": False
}
task2 = {
    "id":  str(uuid.uuid4()),
    "title": "Build API",
    "completed": False
}
task3 = {
    "id":  str(uuid.uuid4()),
    "title": "Test with Postman",
    "completed": True
}

tasks.extend([task1, task2, task3])

# task_id_counter = 4

@app.route("/tasks", methods=["GET"])
def get_tasks():
    return tasks

@app.route("/tasks/<task_id>")
def get_task(task_id):
    for task in tasks:
        if task_id == task["id"]:
             return task
            
    
    return {
        "ERROR": "task not found"
    }, 404

@app.route("/tasks", methods=["POST"])
def create_task():
    global task_id_counter
    title = request.get_json()["title"]
    new_task = {
        "id": str(uuid.uuid4()),
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    return new_task, 201

@app.route("/tasks/<task_id>", methods=["PUT"])
def change_task(task_id):
    data = request.get_json()
    for task in tasks:
            if task_id == task["id"]:
                if "title" in data:
                    task["title"] = data["title"]
                if "completed" in data:
                    task["completed"] = data["completed"]
                return task
    return {
        "ERROR": "bad request"
    }, 400

    
# delete function route
@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            
            return {
                "Message": f"removed task {task["title"]}"
            }
    return {
        "error": "task not found"
    }, 400

if __name__ == "__main__":
    app.run(debug=True)