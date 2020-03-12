from django.urls import path

from user import views

urlpatterns = [
    path('', views.UserCreateView.as_view()),
    path('list/', views.UserListView.as_view()),
    path('<int:pk>', views.UserRetrieveDestroyAPIView.as_view()),
    path('update/<int:pk>', views.UserUpdateView.as_view()),
]
