from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages


def index (request):
	return render(request,'index.html')

def login (request):
	if request.method == 'GET':
		messages.success(request, "Huge success!")
		return render(request,'login.html')
	elif request.method == 'POST':
		if request.POST.get('senha') == 'teste123':
			print('Usuário {} entrou com sucesso!'.format(request.POST.get('email')))
			return redirect(index)
		else:
			print('Usuário {} digitou a senha errada!'.format(request.POST.get('email')))
			return render(request, 'login.html')

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
