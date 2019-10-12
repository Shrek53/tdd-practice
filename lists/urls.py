from django.urls import path
from lists import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]
