from db import get_collection
from bson.objectid import ObjectId
from fastapi import HTTPException
 
def get_all(collection):
    # Return every task currently stored in memory.
    col = get_collection(collection)
    tasks = list(col.find())
    for task in tasks:
        task["_id"] = str(task["_id"])
    return tasks
    

def create(collection, new_entry):
    # `silent=True` lets us raise our own JSON-friendly validation error.
    col = get_collection(collection)
    col.insert_one(new_entry)
    new_entry["_id"] = str(new_entry["_id"])
    return new_entry

def change_task(collection, task_id, changes):
    # Updates accept only the fields this simple API knows how to change.
    col = get_collection(collection)
    try:
        task_id = ObjectId(task_id)
    except Exception:
        raise HTTPException(status_code=400, detail="task id not in correct format")  
     
    result = col.update_one({"_id": task_id}, {"$set": changes})
    
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="task id not found")
    return changes
    
def delete_task(collection, task_id):
    # Delete the matching task and confirm which one was removed.
    col = get_collection(collection)
    # remove task/list  
    try:
        task_id = ObjectId(task_id)
    except Exception:
        raise HTTPException(status_code=400, detail=f"{task_id}not in correct format")  
    
    task = col.find_one({"_id": task_id})
    if task == None:
        raise HTTPException(status_code=404, detail=f"{task_id} not found")
    item_name = task.get("title") or task.get("name")
    col.delete_one({"_id" : task_id})
    # if list remove all items
    
    if collection == "list":
        tasks = get_collection("todo")
        tasks.delete_many({"list": task_id})
    return item_name