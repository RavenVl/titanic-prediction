from django.urls import path
from .views import root, contact
urlpatterns = [
    path('', root, name='root'),
    path('/contact', contact, name='contact'),
]
