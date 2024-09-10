from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Mensaje

def home_view(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from .models import Mensaje

def crear_mensaje_view(request):
    if request.method == 'POST':
        destinatario = request.POST.get('destinatario')
        remitente = request.POST.get('remitente')
        asunto = request.POST.get('asunto')
        contenido = request.POST.get('contenido')

        # Verifica que todos los campos estén presentes
        if destinatario and remitente and asunto and contenido:
            nuevo_mensaje = Mensaje(
                remitente=remitente, 
                destinatario=destinatario,
                asunto=asunto, 
                contenido=contenido
            )
            nuevo_mensaje.save()
            return redirect('ver_MensajesEnviados')  # Asegúrate de usar el nombre correcto en el redirect
        else:
            error_message = "Todos los campos son obligatorios."
            return render(request, 'crear_Mensajes.html', {'error_message': error_message})

    # Si no es POST, renderiza el formulario
    return render(request, 'crear_Mensajes.html')


def ver_mensajes_enviados_view(request):
    mensajes = Mensaje.objects.filter(remitente = 'Sabri')
    return render(request, 'ver_MensajesEnviados.html', {'mensajes': mensajes})


def ver_mensajes_recibidos_view(request):
    mensajes = Mensaje.objects.filter(destinatario='Sabri')
    return render(request, 'ver_MensajesRecibidos.html', {'mensajes': mensajes})

def elegir_mensaje_view(request):
    mensajes = Mensaje.objects.all()  # Obtiene todos los mensajes
    return render(request, 'elegir_mensaje.html', {'mensajes': mensajes})

def eliminar_mensaje_view(request, id):
    mensaje = get_object_or_404(Mensaje, id=id)
    if request.method == 'POST':
        mensaje.delete()
        return redirect('ver_MensajesEnviados')
    return render(request, 'eliminar_Mensajes.html', {'mensaje': mensaje})


