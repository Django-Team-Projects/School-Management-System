from django.urls import path
from . import views

urlpatterns = [
    path('subject-management', views.index, name='subject-management'),
]