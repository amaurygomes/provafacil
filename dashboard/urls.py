from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('questions/', views.questions, name='questions'),
    
   path('question/<int:question_id>/edit/', views.question_edit, name='question_edit'),
   
   path('question/<int:question_id>/delete/', views.question_delete, name='question_delete'),
   
  
]