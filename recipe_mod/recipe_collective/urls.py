from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='collective-home'),
    path('about/', views.about, name='collective-about'),
]