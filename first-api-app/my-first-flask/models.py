import uuid
from db import get_collection
from flask import jsonify, request
from bson.objectid import ObjectId
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity

    
def get_all(collection):
    # Return every task currently stored in memory.
    col = get_collection(collection)
    tasks = list(col.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    
    return jsonify({
        "success": True,
        "data": tasks
    }), 200
    

def get_one(id, collection):
    # Look up a single task and fail with 404 if it does not exist
    col = get_collection(collection)
    if  not ObjectId.is_valid(id):
        raise NotFound(f"{id} not valid id format")
    task =  col.find_one({ "_id": ObjectId(f"{id}") })
    
    if task is None:
        raise NotFound(f"{id} not found")
    else:
        task["_id"] = str(task["_id"]) 
        return jsonify({
            "success": True,
            "task": task
        }), 200


def create(collection):
    # `silent=True` lets us raise our own JSON-friendly validation error.
    col = get_collection(collection)
    data = request.get_json(silent=True)
    new_entry = None
    if not data or not isinstance(data, dict):
            raise BadRequest("request body must be json")
        
    if collection == "todo":
        if "title" not in data:
            raise BadRequest("title is required")
        title = data["title"]
        if not isinstance(title, str):
            raise BadRequest("title must be a string")
        if not title.strip():
            raise UnprocessableEntity("title must contain text")
    
        # New tasks get a generated id and start as incomplete.
        new_entry = {
        "title": title.strip(),
        "completed": False,
        "list": data.get("list")
            }
    elif collection == "list":
        if "name" not in data:
            raise BadRequest("name is required")
        if not isinstance(data["name"], str):
            raise BadRequest("name must be a string")
        if not data["name"].strip():
            raise UnprocessableEntity("name must contain text")
        #add list entry
        new_entry = {
            "name": data["name"]  
        }
    
    else:
        return jsonify("error"), 400
    if new_entry:
        col.insert_one(new_entry)
        new_entry["_id"] = str(new_entry["_id"])
        return jsonify({
            "success": True,
            "data": new_entry
        }), 201

def change_task(task_id, collection):
    # Updates accept only the fields this simple API knows how to change.
    col = get_collection(collection)
    if  not ObjectId.is_valid(task_id):
        raise NotFound(f"{task_id} not valid id format")
    
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        raise BadRequest("error: update request must contain data")
    if collection == "todo":
        keys = ("title", "completed", "list")
    if collection == "list":
        keys = ("name",)
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
    
    if "name" in data:
        if not isinstance(data["name"], str):
            raise BadRequest("name must be a string")
        if not data["name"].strip():
            raise UnprocessableEntity("name must contain text")
        # Trim whitespace so stored titles stay clean.
        updates.update({"name": data["name"].strip()})
    
    if "list" in data:
        if not isinstance(data["list"], str):
            raise BadRequest("list must be a string")
        if not data["list"].strip():
            raise UnprocessableEntity("list must contain text")
        updates.update({"list": data["list"].strip()})
        
        
    if updates:
        col.update_one({"_id": ObjectId(task_id)}, {"$set": updates})
        return jsonify({
            "success": True,
            "updates": updates
        }), 200
    
def delete_task(task_id, collection):
    # Delete the matching task and confirm which one was removed.
    col = get_collection(collection)
    if  not ObjectId.is_valid(task_id):
        raise NotFound(f"{task_id} not valid id format")
    # remove task/list  
    task = col.find_one({"_id": ObjectId(task_id)})
    if task == None:
        raise NotFound(f"{task_id} not found")
    col.delete_one({"_id" : ObjectId(task_id)})
    # if list remove all items
    item_name = task.get("title") or task.get("name")
    if collection == "list":
        tasks = get_collection("todo")
        tasks.delete_many({"list": task_id})
    return jsonify({
        "Message": f"removed {item_name}"
    }), 200
    