from django.urls import path
from m6_todo_app.views import (
    new_task,
    task_datas
)

urlpatterns = [
    path('new/', new_task, name='new_task'),
    path('datas/<int:pk>/', task_datas, name='task_datas')
]
