from django.urls import path
from m6_todo_app.views import (
    new_task
)

urlpatterns = [
    path('new/', new_task, name='new_task')
]
