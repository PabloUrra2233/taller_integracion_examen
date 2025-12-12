from django.urls import path
from .views import lista_productos, detalle_producto, crear_producto, eliminar_producto

urlpatterns = [
    path('', lista_productos, name='lista_productos'),
    path('producto/nuevo/', crear_producto, name='crear_producto'),
    path('producto/<int:pk>/', detalle_producto, name='detalle_producto'),
    path('producto/<int:pk>/eliminar/', eliminar_producto, name='eliminar_producto'),
]
