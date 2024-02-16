from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('lista/', views.lista, name='lista')
   
  
]