from django.db import models

# Create your models here.
class Usuario(models.Model):
	nombre = models.CharField(max_length=20)
	apellidos = models.CharField(max_length=30)
	usuario = models.CharField(max_length=10)
	contrasena = models.CharField(max_length=10)

	def __unicode__(self):
		return self.nombre
