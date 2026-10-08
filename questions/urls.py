from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name='catalog'),
    path('exam/<str:cert_id>/<str:exam>/',
         views.question_list, name='question_list'),
    path('syllabus/<str:cert_id>/', views.syllabus, name='syllabus'),
    path('chapter/<str:cert_id>/<int:number>/',
         views.chapter, name='chapter'),
]
