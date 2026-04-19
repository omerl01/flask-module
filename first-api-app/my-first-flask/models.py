import uuid
from db import get_collection
from flask import jsonify, request
from bson.objectid import ObjectId
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity

    
def get_tasks():
    # Return every task currently stored in memory.
    col = get_collection("todo")
    tasks = list(col.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    
    return jsonify({
        "success": True,
        "data": tasks
    }), 200
    

def get_task(task_id):
    # Look up a single task and fail with 404 if it does not exist
    col = get_collection("todo")
    if  not ObjectId.is_valid(task_id):
        raise NotFound(f"{task_id} not valid id format")
    task =  col.find_one({ "_id": ObjectId(f"{task_id}") })
    
    if task is None:
        raise NotFound(f"{task_id} not found")
    else:
        task["_id"] = str(task["_id"]) 
        return jsonify({
            "success": True,
            "task": task
        }), 200


def create_task():
    # `silent=True` lets us raise our own JSON-friendly validation error.
    col = get_collection("todo")
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        raise BadRequest("request body must be json")
    if "title" not in data:
        raise BadRequest("title is required")
    title = data["title"]
    if not isinstance(title, str):
        raise BadRequest("title must be a string")
    if not title.strip():
        raise UnprocessableEntity("title must contain text")

    # New tasks get a generated id and start as incomplete.
    new_task = {
    "title": title.strip(),
    "completed": False
        }
    
    col.insert_one(new_task)
    new_task["_id"] = str(new_task["_id"])
    return jsonify({
         "success": True,
        "data": new_task
    }), 201

def change_task(task_id):
    # Updates accept only the fields this simple API knows how to change.
    col = get_collection("todo")
    if  not ObjectId.is_valid(task_id):
        raise NotFound(f"{task_id} not valid id format")
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        raise BadRequest("error: update request must contain data")
    keys = ("title", "completed")
    data_keys = data.keys()
    for key in data_keys:
        if key not in keys:
            raise BadRequest(f"not allowed to pass {key}")
    task = col.find_one({"_id": ObjectId(task_id)})
    if task == None:
        raise NotFound(f"{task_id} not found")
    updates = {}
    if "title" in data:
        if not isinstance(data["title"], str):
            raise BadRequest("title must be a string")
        if not data["title"].strip():
            raise UnprocessableEntity("title must contain text")
        # Trim whitespace so stored titles stay clean.
        updates.update({"title": data["title"].strip()})
    if "completed" in data:
        if not isinstance(data["completed"], bool):
            raise BadRequest("completed must be a boolean")
        updates.update({"completed": data["completed"]})
    if updates:
        col.update_one({"_id": ObjectId(task_id)}, {"$set": updates})
        return jsonify({
            "success": True,
            "task_updates": updates
        }), 200
    
def delete_task(task_id):
    # Delete the matching task and confirm which one was removed.
    col = get_collection("todo")
    if  not ObjectId.is_valid(task_id):
        raise NotFound(f"{task_id} not valid id format")
        
    task = col.find_one({"_id": ObjectId(task_id)})
    if task == None:
        raise NotFound(f"{task_id} not found")
    col.delete_one({"_id" : ObjectId(task_id)})

    return jsonify({
        "Message": f"removed task {task['title']}"
    }), 200
    