from django.urls import path
from . import views

urlpatterns = [
    path("", views.getTodo),
    path("add/", views.addTodo, name="add"),
    path("register", views.register),
    path("login/", views.Login, name="login"),
    path("delete/<int:todo_id>/", views.delete, name="delete"),
    path("edit_task/<int:todo_id>/", views.editTask, name="update"),
    path("subtasks/<int:todo_id>/", views.view_subtasks, name="view_subtasks"),
    path("subtasks/add/<int:todo_id>/", views.add_subtask, name="subtaskAdd"),
    path(
        "subtasks/<int:todo_id>/delete/<int:subtask_id>/",
        views.delete_subtask,
        name="subtaskDelete",
    ),
    path(
        "subtasks/update/<int:todo_id>/<int:subtask_id>/",
        views.update_subtask,
        name="subtaskUpdate",
    ),
]