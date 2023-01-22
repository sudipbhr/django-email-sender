from django.urls import path
from sender import views


urlpatterns = [
    path('', views.home, name="home"),
    path('sender/', views.sender, name="sender")
]
