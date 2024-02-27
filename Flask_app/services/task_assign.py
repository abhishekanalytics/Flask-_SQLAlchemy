from flask_app.models.models import Status
from .. import db
from flask_app.services.tasks import get_task_by_id

# def assign_task(task_id, user_id):
#     task = get_task_by_id(task_id)
#     task.assigned_to = user_id
#     task.status = Status.RUNNING.value
#     db.session.commit()
