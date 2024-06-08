from django.urls import path
from . import views

urlpatterns = [
     path('registration/', views.RegistrationView.as_view()),
     path('authorization/', views.AuthorizationView.as_view()),
     path('login/', views.LoginView.as_view())
]