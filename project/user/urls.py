from django.urls import path
from .views import singup, login

urlpatterns = [
    path('login/', login),
    path('signup/', singup),
]