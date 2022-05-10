from django.urls import path
from . import views

urlpatterns = [
    path("", views.Projects, name="projects"),
    path("project/<str:pk>/", views.Project, name="project"),
]