from django.urls import path
from .views import index_titanic, result
app_name = 'titanic'
urlpatterns = [
    path('', index_titanic, name='index_titanic'),
    path('result/', result, name='result_titanic')
]

