from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('index1/', views.index1),
    path('students/', views.StudentModelView.as_view()),
    path('students/<int:id>', views.StudentModelView.as_view()),
    path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),          # Authentication
    path('register/', views.register),                                                      # register

]
























