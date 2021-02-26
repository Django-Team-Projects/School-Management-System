from django.urls import path
from . import views

urlpatterns = [
    path('student-management', views.index, name='student-management'),
]