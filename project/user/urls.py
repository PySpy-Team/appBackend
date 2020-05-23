from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('signup/', views.singup),
    path('update/', views.update),
    path('challenges/', views.get_user_challenges)
]