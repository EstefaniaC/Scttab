from django.db import models

# Create your models here.
class Registro_Solicitante(models.Model):
	nombre = models.CharField(max_length=50)
	empresa = models.CharField(max_length=50)
	folio_oficio = models.CharField(max_length=50)
	fecha_recibido = models.DateField()
	asunto = models.TextField(max_length=200)
	modalidad = models.CharField(max_length=50)
	numero_registro = models.IntegerField()
	municipio = models.CharField(max_length=50)
	coordinador = models.CharField(max_length=50)
	fecha_entrega_DGTEC = models.DateField()
	observacion = models.TextField(max_length=200)	
