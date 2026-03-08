from . import views
from django.urls import path

urlpatterns = [
    path('productos/', views.lista_productos, name='productos'),
    path('productos/nuevo/', views.nuevo_producto, name='nuevo_producto'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_producto'),
    path('productos/anular/<int:id>/', views.eliminar_producto, name='anular_producto'),

]