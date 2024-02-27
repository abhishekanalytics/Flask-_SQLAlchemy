from flask import request, jsonify
from flask.views import MethodView
from flask_app.models.models import Task
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
    )
from ..decorators.decorator import (
    admin_required,manager_required
    )
from flask_app.services.tasks import (
    create_task,
    get_all_tasks, 
    get_task_by_id,
    update_task,
    delete_task
)



class TaskView(MethodView):
    # decorators = [jwt_required()]



    def __init__(self, model: Task = None) -> None:
        self.model = model





    def post(self):
        title = request.json.get("title", None)
        description = request.json.get("description", "")
        if title is None:
            return jsonify(message="Invalid title") , 400
        try:
            task = create_task(
                model = self.model,
                title = title,
                description = description
                )
            return jsonify(message="Task added successfully")
        except IntegrityError:
            return jsonify(message="The given id already exists")
        

    def get(self, id=None):
        if not id:
            tasks = get_all_tasks()
            task_list = [
                {
                    "id": task.id,
                    "title": task.title,
                    "description":task.description,                   
                    } 
                    for task in tasks
                ]
            return jsonify({"tasks": task_list})
        else:
            task = get_task_by_id(id)
            if not task:
                return jsonify({"message": "task not found"}), 404
            task_data = {
                "id": task.id, 
                "title": task.title,
                  "description": task.description
                }
            return jsonify({"task": task_data}) 
    


    def patch(self, id):
        task = get_task_by_id(id)
        if not task:
            return jsonify({"message": "Task not found"}), 404        
        new_data = request.json
        update_task(task, new_data) 
        return jsonify({"message": "Task updated successfully"})



    def delete(self,id):
        task = get_task_by_id(id)
        if not task:
            return jsonify({"message": "Task not found"}), 404
        delete_task(task)
        return jsonify({"message": "Task deleted successfully"})