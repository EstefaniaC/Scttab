from django.db import models


class revision(models.Model):
	numero_registro = models.IntegerField()
	observacion = models.TextField(max_length=100)