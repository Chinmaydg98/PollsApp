from django.urls import path
from . import views


APP_NAME = 'polls'

urlpatterns = [
    path('', views.index, name='index')
]
