from flask import request, jsonify, Blueprint
from werkzeug.exceptions import NotFound, BadRequest, Conflict, UnprocessableEntity
import models
import uuid
from bson.objectid import ObjectId

tasks_bp = Blueprint("tasks", __name__)


@tasks_bp.route("/all/<collection>", methods=["GET", "POST"])
def get_tasks(collection):
    if request.method == "GET":
        return models.get_all(collection)
    elif request.method =="POST":
        return models.create(collection)
    else:
        raise BadRequest("request type not supported")

@tasks_bp.route("/item/<task_id>/<collection>", methods=["GET", "PUT", "DELETE"])
def get_one(task_id, collection):
    if request.method == "GET":
        return models.get_one(task_id, collection)
    elif request.method == "PUT":
        return models.change_task(task_id, collection)
    elif request.method == "DELETE":
        return models.delete_task(task_id, collection)
    else:
        raise BadRequest("action not supported")
