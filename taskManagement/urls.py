from django.urls import path
from .views import index_task

app_name = 'taskManagement'

urlpatterns = [
    path('', index_task, name='index_task'),
]

