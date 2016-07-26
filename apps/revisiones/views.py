from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def revision(request):
	return render(request, 'revision.html')

def revision_oficio(request):
	return render(request, 'revision_oficios.html')

