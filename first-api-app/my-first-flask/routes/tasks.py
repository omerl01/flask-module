from fastapi import APIRouter
from schemas import Tasks
import models

router = APIRouter()
collection = "todo"

@router.get("/tasks")
def get_all_tasks():
    return models.get_all(collection)

@router.post("/tasks", status_code=201)
def create_task(l: Tasks):
    return models.create(collection, l.model_dump())

@router.put("/tasks/{task_id}")
def change_task(task_id: str, t: Tasks):
    return models.change_task(collection, task_id, t.model_dump())


@router.delete("/tasks/{task_id}")
def delete(task_id):
    return models.delete_task(collection, task_id)
