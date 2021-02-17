from django.shortcuts import render , HttpResponse

# Create your views here.

def index(request):
    
    
    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Proyecto Web con DJango',
    })

def region(request):
    
    
    return render(request, 'index.html', {
        'titulo': 'REGIONES',
        'mensaje': 'Listado de Regiones',
    })

def create_region(request):
    
    
    return render(request, 'index.html', {
        'titulo': 'CREAR REGION',
        'mensaje': 'Agregar Región',
    })

def empleado(request):
    
    
    return render(request, 'index.html', {
        'titulo': 'EMPLEADOS',
        'mensaje': 'Listado de Trabajadores',
    })

def create_empleado(request):
    
    
    return render(request, 'index.html', {
        'titulo': 'CREAR EMPLEADO',
        'mensaje': 'Agregar Trabajador',
    })