from typing import Any
from ..models.models import Task,User
from .. import db


def create_task(model: Any, title: str, description: str, user: User):
    task = model(
        title=title,
        description=description,
        assigned_to=user.id
    )
    db.session.add(task)
    db.session.commit()
    return task

def get_all_tasks():
    return Task.query.all()


def get_task_by_id(id):
    task = Task.query.get(id)
    if task is None:
        return None 
    return task



def update_task(
    task, 
    new_data
    ):
    task.title = new_data.get(
    "title",        
    task.title
    )
    task.description = new_data.get(
    "description",
    task.description
    )
    db.session.commit()


def delete_task(task):
    db.session.delete(task)
    db.session.commit()