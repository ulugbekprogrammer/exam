from django.urls import path
from .views import *

urlpatterns = [
    path('', base_view, name='home'),
    path('result', result, name='result')
]