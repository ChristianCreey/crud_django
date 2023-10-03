from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_materias, name="listar_materias"),
    path('registrarMateria/', views.registrarMateria, name="registrar_materia"),
    path('leer/<int:id>/', views.leer, name="leer_materia"),
    path('editar/<int:id>/', views.editar, name='editar_materia'),
    path('eliminar/<int:id>/', views.eliminar, name='eliminar_materia'),
]