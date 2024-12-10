from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView

app_name = 'itreporting'  # Define the namespace for the app

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # This is your contact page URL
    path('report/', PostListView.as_view(), name='report'),
    path('issues/<int:pk>/', PostDetailView.as_view(), name='issue-detail'),  # Add the trailing slash
    path('issue/new', PostCreateView.as_view(), name = 'issue-create'),
    path('issue/<int:pk>/delete/', PostDeleteView.as_view(), name = 'issue-delete'),

]


