from django.urls import path
from . import views

app_name = 'itreporting'  # Define the namespace for the app

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # This is your contact page URL
]