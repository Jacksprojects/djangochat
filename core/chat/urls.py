from django.urls import path

from . import views

app_name = "chat"

urlpatterns = [
  path('', views.index, name='index'),
  path('accounts/register/', views.register, name='register'),
  path('<str:room_name>/', views.room, name='room'),
]