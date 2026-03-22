from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
   path('', views.cadastrar_usuario, name='cadastro'),
   path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
   path('deletar/<int:id>/', views.deletar_usuario, name='deletar_usuario'),
]
