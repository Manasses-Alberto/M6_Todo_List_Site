from django.urls import path
from m6_todo_app.views import (
    new_task,
    task_datas,
    edit_task,
    delete_task
)

urlpatterns = [
    path('new/', new_task, name='new_task'),
    path('datas/<int:pk>/', task_datas, name='task_datas'),
    path('edit/<int:pk>/', edit_task, name='edit_task'),
    path('delete/<int:pk>/', delete_task, name='delete_task')
]
