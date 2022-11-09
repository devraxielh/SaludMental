from django.shortcuts import render
from django.http import HttpRequest
from .models import Test

# Create your views here.
def index(request):
    title = 'Pagina de inicio...'
    tests = Test.objects.all()
    return render(request, 'PaginaSaludMental/index.html', {
        'title': title,
        'tests':tests,
    })

def login(request):
    return render(request, 'PaginaSaludMental/login.html', {
        'title': 'Iniciar Sesion',
        'descripcion': 'Ingrese sus datos para iniciar sesion'
    })

def register(request):
    return render(request, 'PaginaSaludMental/registarse.html', {
        'title': 'Registrase',
        'descripcion': 'Ingrese sus datos para registrarse'
    })

def contact(request):
    return render(request, 'PaginaSaludMental/contactenos.html', {
        'title': 'Contactenos',
        'descripcion': 'Ingrese sus datos para contactarnos'
    })

def list_test(request):
    tests = Test.objects.all()
    return render(request, 'PaginaSaludMental/list_test.html', {
        'title': 'Test´s',
        'descripcion': 'Listado de tests activos en la plataforma',
        'tests':tests
    })

def home(request):
    title = 'Django!!'
    return render(request, 'home.html', {
        'title': title
    })