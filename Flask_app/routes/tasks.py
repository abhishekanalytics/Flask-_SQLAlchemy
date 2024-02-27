from flask import Blueprint
from flask_app.models.models import Task
from ..views.tasks import TaskView


task_bp = Blueprint('task_bp', __name__, url_prefix='/tasks')


task_bp.add_url_rule(
    rule='/task',
    view_func=TaskView.as_view(
        "get_all_tasks",
        model=Task
    )
)



task_bp.add_url_rule(
    rule = '/task/<id>',
    view_func = TaskView.as_view(
        "display_update_delete",
        model = Task
    )
)
