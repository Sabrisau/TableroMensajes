from django.urls import path
from mensajes import views

urlpatterns = [
    path('crear/', views.crear_mensaje_view, name='crear_mensaje'),
    path('recibidos/', views.ver_mensajes_recibidos_view, name='ver_mensajes_recibidos'),
    path('enviados/', views.ver_mensajes_enviados_view, name='ver_mensajes_enviados'),
    path('eliminar/<int:id>/', views.eliminar_mensajes_views, name='eliminar_mensaje'),
]
