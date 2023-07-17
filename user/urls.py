from django.urls import path
from . import views

from django.urls import path, re_path


urlpatterns = [
    # path('dashboard/', views.dashboard, name="dashboard")
    
    path("", views.register, name="register"),
    path("sots/volunteers/", views.volunteers, name="volunteers"),
]