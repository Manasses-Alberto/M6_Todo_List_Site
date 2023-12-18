from django.contrib import admin
from django.urls import path, include
from m6_todo_app.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('auth/', include('m6_todo_app.urls.auth'))
]
