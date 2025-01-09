from django.urls import path
from . import views 
from .views import (ModuleListView, ModuleDetailView, ModuleCreateView, ModuleDeleteView, module_list )

app_name = 'itreporting'  

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  
    path('modules/', module_list, name='module_list'),  
    path('modules/<int:pk>/', views.ModuleDetailView.as_view(), name='module_detail'),  
    path('modules/add/', views.ModuleCreateView.as_view(), name='module-add'),  
    path('modules/<int:pk>/delete/', views.ModuleDeleteView.as_view(), name='module-delete'),  
    path('register/', views.register_for_course, name='course-register'), 
    path('profile/', views.profile, name='profile'), 



]


