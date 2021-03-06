from todolist.models import Task
from django.urls import path
from .views import index, update_task, delete_task, task_detail

urlpatterns = [
    path('', index, name="index"),
    path("update/<int:pk>/", update_task, name="update-task"),
    path("delete/<int:pk>/", delete_task, name="delete_task"),
    path("detail/<int:id>/", task_detail, name="task_detail")

]   