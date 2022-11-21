from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.file_upload),
    path('upload-images', views.upload_images, name='image_upload'),
    path('new/project', views.add_project, name='project_add'),
]