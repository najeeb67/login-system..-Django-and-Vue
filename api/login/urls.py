from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('register/<int:user_id>/', views.get_register , name="get_register")
]
