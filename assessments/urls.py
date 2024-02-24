from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new_assessment'),
    # Add other URL patterns for the app here
]
