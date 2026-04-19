from flask import request, jsonify, Blueprint
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
import models
import uuid
from db import get_collection
from bson.objectid import ObjectId

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/tasks", methods=["GET", "POST"])
def get_tasks():
    if request.method == "GET":
        return models.get_tasks()
    if request.method =="POST":
        return models.create_task()
    else:
        raise BadRequest("request type not supported")

@tasks_bp.route("/tasks/<task_id>", methods=["GET", "PUT", "DELETE"])
def get_task(task_id):
    if request.method == "GET":
        return models.get_task(task_id)
    elif request.method == "PUT":
        return models.change_task(task_id)
    elif request.method == "DELETE":
        return models.delete_task(task_id)
    else:
        raise BadRequest("action not supported")
