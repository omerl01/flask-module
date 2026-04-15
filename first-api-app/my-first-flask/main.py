from flask import Flask, request, jsonify
from datetime import datetime, timezone
import uuid
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
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
# create errorhundle for not found errors
@app.errorhandler(NotFound)
def not_found(e):
    return jsonify({
        "ERROR": str(e)
    }), 404

# create errorhundle forBadrequest errors  
@app.errorhandler(BadRequest)
def bad_request(e):
    return jsonify({
        "ERROR": str(e)
    }), 400

# create errorhundle forunprocessable entries errors
@app.errorhandler(UnprocessableEntity)
def empty_strings(e):
    return jsonify({
        "ERROR": str(e)
    }), 400

# create route for getting all tasks
@app.route("/tasks", methods=["GET"])
def get_tasks():
    return tasks

# route for getting task by id
@app.route("/tasks/<task_id>", methods=["GET"])
def get_task(task_id):
    for task in tasks:
        if task_id == task["id"]:
             return task
    raise NotFound(f"{task_id} not found")  

# create a task
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if data == {}:
        raise BadRequest("request body must be json")
    title = data["title"]
    if not isinstance(title, str):
        raise BadRequest("title must be a string")
    if not title.strip():
        raise UnprocessableEntity("title must contain text")
    new_task = {
    "id": str(uuid.uuid4()),
    "title": title.strip(),
    "completed": False
        }
    tasks.append(new_task)
    return jsonify({
        "success": True,
        "data": new_task
    }), 201
        
# update a task
@app.route("/tasks/<task_id>", methods=["PUT"])
def change_task(task_id):
    data = request.get_json()
    keys = ("title", "completed")
    data_keys = data.keys()
    if not data:
        raise BadRequest("error: update request must contain data")
    for key in data_keys:
        if key not in keys:
            raise BadRequest(f"not allowed to pass {key}")
    for task in tasks:
            if task_id == task["id"]:
                if "title" in data:
                    task["title"] = data["title"]
                if "completed" in data:
                    task["completed"] = data["completed"]
                return task
    raise NotFound(f"{task_id} not found")
    
# delete function route
@app.route("/tasks/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            
            return {
                "Message": f"removed task {task["title"]}"
            }
    raise NotFound(f"{task_id} not found")

if __name__ == "__main__":
    app.run(debug=True)