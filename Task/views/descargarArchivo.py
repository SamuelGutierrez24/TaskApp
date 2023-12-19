from django.views.generic.base import View
from django.http import HttpResponse
from Task.models import *

class DescargarArchivoView(View):
    
    def post(self, request, *args, **kwargs):
        id_tarea = request.POST['id_tarea'] # Obtener el id de la tarea
        nombre_archivo = request.POST['nombre_archivo'] # Obtener el nombre del archivo
        tarea = Task.objects.get(pk=id_tarea) # Obtener la tarea
        extra = ExtraData.objects.get(task=tarea, archive=nombre_archivo) # Obtener el objeto ExtraData que tiene el archivo
        response = HttpResponse(extra.archive, content_type='application/octet-stream') # Crear una respuesta con el contenido del archivo
        response['Content-Disposition'] = 'attachment; filename="%s"' % extra.archive # Agregar un encabezado para indicar que es un archivo adjunto
        return response # Devolver la respuesta
