from django.urls import path
from .views import root, contact

app_name = 'first_app'

urlpatterns = [
    path('', root, name='root'),
    path('contact', contact, name='contact'),
]
