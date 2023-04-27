## Library App

Tiene una lista de libros. Puede listar/eliminar/editar un libro.
El libro tiene: identificación del libro, nombre, autor, año.

## Requerimientos
Para ejecutar el proyecto, se requiere tener instalados:
- Python v3.8
- virtualenv
- Gestor de Base de Batos (MySQL)

### Creación del Entorno
Para la creación del entorno virtual se deben ejecutar los siguientes comandos
en la carpeta del proyecto:

```
virtualenv -p  python3 env
.\env\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Creación de la Base de Datos
Para que la migración funcione, deben crear una base de datos llamada ```django_api```

## Ejecutar Migración

```
python manage.py migrate
python manage.py makemigrations
```