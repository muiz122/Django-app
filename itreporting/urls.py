from django.urls import path
from . import views 
from .views import (ModuleListView, ModuleDetailView, ModuleCreateView, ModuleDeleteView, )

app_name = 'itreporting'  # Define the namespace for the app

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # This is your contact page URL
    path('modules/', views.ModuleListView.as_view(), name='module-list'),  # List all modules
    path('modules/<int:pk>/', views.ModuleDetailView.as_view(), name='module-detail'),  # View details of a specific module
    path('modules/add/', views.ModuleCreateView.as_view(), name='module-add'),  # Add a new module
    path('modules/<int:pk>/delete/', views.ModuleDeleteView.as_view(), name='module-delete'),  # Delete a module
    path('register/', views.register_for_course, name='course-register'), 





]


