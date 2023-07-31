from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot, name = 'chatbot'),
    path('login', views.chatbot, name = 'login'),
    path('register', views.chatbot, name = 'register'),
    path('logout', views.chatbot, name = 'logout')
]