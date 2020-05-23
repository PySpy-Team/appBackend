from django.urls import path
from . import views


urlpatterns = [
    path('<int:id>/', views.get_challenge),
    path('create/', views.create_challenge),
    path('<int:id>/answers/', views.get_answers)
]