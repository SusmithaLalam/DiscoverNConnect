from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='profiles-home'),
    path('about/', views.about, name='profiles-about')
]