from django.urls import path
from . import views

urlpatterns = [
    path('employee-management', views.index, name='employee-management'),
]