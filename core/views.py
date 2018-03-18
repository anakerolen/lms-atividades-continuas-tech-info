from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return render(request,'index.html')

def login (request):
	if request.method == 'GET':
		print('Acesso via GET')
		
	else:
		print('Acesso via POST')
	
	return render(request,'login.html')

# Create your views here.
