from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('script/<int:pk>/', views.script_detail, name='script_detail'),
]