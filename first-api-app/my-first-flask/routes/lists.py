from fastapi import APIRouter
from schemas import Lists
import models

list_router = APIRouter()
collection = "list"

@list_router.get("/lists")
def get_all_lists():
    return models.get_all(collection)
    
@list_router.post("/lists", status_code=201)
def create_list(l: Lists):
    return models.create(collection, l.model_dump())


@list_router.put("/lists/{list_id}")
def change_list(list_id: str, l: Lists):
    return models.change_task(collection, list_id, l.model_dump())

@list_router.delete("/lists/{list_id}")
def delete(list_id: str):
    return models.delete_task(collection, list_id)
