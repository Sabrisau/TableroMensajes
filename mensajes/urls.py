from django.urls import path
from .views import crear_mensaje

urlpatterns = [
    path('crear/', crear_mensaje, name='crear_mensaje'),
    path('recibidos/', ver_mensajes_recibidos, name='ver_mensajes_recibidos'),
    path('enviados/', ver_mensajes_enviados, name='ver_mensajes_enviados'),
    path('eliminar/<int:id>/', eliminar_mensajes, name='eliminar_mensaje'),
]
