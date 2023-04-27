import json
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import Libro

class LibroView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0):
        if (id > 0):
            libros = list(Libro.objects.filter(id=id).values())
            if len(libros) > 0:
                libro = libros[0]
                datos = {'message': "Success", 'libros': libro}
            else: 
                datos = {'message': "No hay libros"}
            return JsonResponse(datos)
        else:
            libros = list(Libro.objects.values())
            if len(libros) > 0:
                datos = {'message': "Success", 'libros': libros}
            else: 
                datos = {'message': "No hay libros"}
            return JsonResponse(datos)
    
    def put(self, request, id):
        jd = json.loads(request.body)
        libros = list(Libro.objects.filter(id=id).values())
        if len(libros) > 0:
            libro = Libro.objects.get(id=id)
            libro.name=jd['name']
            libro.author=jd['author']
            libro.year=jd['year']
            libro.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encuentra el registro"}    
        return JsonResponse(datos)
    
    def delete(self, request, id):
        libros = list(Libro.objects.filter(id=id).values())
        if len(libros) > 0:
            Libro.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "No se encuentra el registro"}   
        return JsonResponse(datos)
    