from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('exam/<str:exam>/', views.question_list, name='question_list'),
]
