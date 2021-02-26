from django.urls import path
from . import views

urlpatterns = [
    path('school-management', views.index, name='school-management'),
]