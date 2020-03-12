from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from department import views

urlpatterns = [
    path('', views.DepartmentListCreateView.as_view()),
    path('<int:pk>', views.DepartmentRetrieveUpdateDestroyView.as_view()),
]