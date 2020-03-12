from django.urls import path

from auth2 import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
]
