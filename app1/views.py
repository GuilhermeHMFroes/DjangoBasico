from django.shortcuts import render
from django.http import HttpResponse
from .forms import Formulario

# Create your views here.

def index(request):
    return render(request, 'index.html')

def w3c(request):
    return render(request, 'w3c.html')

def HTML(request):
    return render(request, 'HTML.html')

def CSS(request):
    return render(request, 'CSS.html')

def JavaScript(request):
    return render(request, 'JavaScript.html')

def Frontend(request):
    return render(request, 'Frontend.html')

def Backend(request):
    return render(request, 'Backend.html')


def formulario(request):

    if request.method == 'POST':
        form = Formulario(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Mensagem: {mensagem}')
        else:
            print("Formulário inválido. Erros de validação:")
            print(form.errors)

    else:
        form = Formulario()

    context = {
        'form': form
    }

    return render(request, 'formulario.html', context)
