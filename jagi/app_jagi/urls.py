from django.urls import path
from . import views

urlpatterns = [
    path('', views.jagi_list, name='jagi_list'),
]
