from django.urls import path
from .views import LibroView

urlpatterns=[
    path('libros/', LibroView.as_view(), name='lista_libros'),
    path('libros/<int:id>', LibroView.as_view(), name='obtener_libro')
]