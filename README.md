# Proyecto Tablero de Mensajes
Este proyecto es una aplicación web desarrollada con Django para gestionar el envío y recepción de mensajes. Incluye funcionalidades para crear, ver y eliminar mensajes.

## Requisitos
- Python 3.8 o superior
- Django 4.2 o superior

## Instalación
Sigue estos pasos para instalar y configurar el proyecto en tu entorno local:

1. Clona el repositorio:git clone https://github.com/tu-usuario/tu-repo.git
2. Insatala las dependencias: pip install -r requirements.txt
3. Realiza las migraciones de la base de datos: python manage.py migrate
4. Inicia el servidor: python manage.py runserver

## Uso
Muestra la página principal de la aplicación: http://127.0.0.1:8000/
Permite crear nuevos mensajes: http://127.0.0.1:8000/crear/
Muestra los mensajes enviados por el usuario: http://127.0.0.1:8000/enviados/
Muestra los mensajes recibidos por el usuario: http://127.0.0.1:8000/recibidos/
Permite eliminar un mensaje específico: http://127.0.0.1:8000/eliminar/<id>/
