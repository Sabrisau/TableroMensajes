from django.urls import path
from mensajes import views
from .views import CrearMensajeView

urlpatterns = [
    path('', views.home_view, name='home'),
    path('crear/', CrearMensajeView.as_view(), name='crear_Mensajes'),
    path('recibidos/', views.ver_mensajes_recibidos_view, name='ver_MensajesRecibidos'),
    path('enviados/', views.ver_mensajes_enviados_view, name='ver_MensajesEnviados'),
    path('eliminar/', views.elegir_mensaje_view, name='elegir_mensaje'),
    path('eliminar/<int:id>/', views.eliminar_mensaje_view, name='eliminar_Mensajes'),
]
