from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.file_upload),
    path('view-images/', views.ImagePageView.as_view(), name='images'),
    path('view-projects/', views.ProjectPageView.as_view(), name='projects'),
    path('add-project/', views.ProjectCreateView.as_view(), name='project_add'),
    path('change-project/', views.ProjectUpdateView.as_view(), name='project_change'),
    path('delete-project/', views.ProjectDeleteView.as_view(), name='project_delete'),
]