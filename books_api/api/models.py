from django.db import models

class Libro(models.Model):
    name=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    year=models.PositiveIntegerField(default=int)
