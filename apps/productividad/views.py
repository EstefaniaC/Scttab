from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def productividad(request):
	return render(request, 'productividad.html')