from django.shortcuts import render, redirect
from .forms import MensajeForm
from django.shortcuts import get_object_or_404
from .models import Mensaje

def crear_mensaje_view(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_mensajes_enviados')  # Redirigir a otra vista
    else:
        form = MensajeForm()
    return render(request, 'mensajes/crear_mensaje.html', {'form': form})

def ver_mensajes_recibidos_view(request):
    mensajes = Mensaje.objects.filter(destinatario=request.user.username)
    return render(request, 'mensajes/mensajes_recibidos.html', {'mensajes': mensajes})

def ver_mensajes_enviados_views(request):
    mensajes = Mensaje.objects.filter(remitente=request.user.username)
    return render(request, 'mensajes/mensajes_enviados.html', {'mensajes': mensajes})

def eliminar_mensaje_views(request, id):
    mensaje = get_object_or_404(Mensaje, id=id)
    if request.method == 'POST':
        mensaje.delete()
        return redirect('ver_mensajes_recibidos')
    return render(request, 'mensajes/eliminar_mensaje.html', {'mensaje': mensaje})
