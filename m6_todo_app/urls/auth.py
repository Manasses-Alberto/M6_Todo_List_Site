from django.urls import path
from m6_todo_app.views import login, register

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register')
]
