from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse

def contato(request):
	if request.method == 'GET':
		return render(request, 'contato.html')
	elif request.method == 'POST':
		print(request.POST.get('nomeCompleto'))
		print(request.POST.get('emailRemetente'))
		print(request.POST.get('assunto'))
		print(request.POST.get('mensagem'))
		return render(request, 'contato.html')
	else:
		return request(request, 'contato.html')
# Create your views here.
