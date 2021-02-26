from django.urls import path
from . import views

urlpatterns = [
    path('teacher-management', views.index, name='teacher-management'),
]