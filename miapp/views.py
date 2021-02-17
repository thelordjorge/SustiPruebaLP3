from django.shortcuts import render , HttpResponse, redirect
from miapp.models import Region
from miapp.models import Empleado
from django.db.models import Q
from miapp.forms import FormRegion
from miapp.forms import FormEmpleado
from django.contrib import messages
# Create your views here.

def index(request):
    
    
    return render(request, 'index.html', {
        'titulo': 'Inicio',
        'mensaje': 'Proyecto Web con DJango',
    })

def region(request):
    
    
    regiones = Region.objects.all()
    
    return render(request, 'region.html',{
        'regiones': regiones,
        'titulo': 'Listado de Regiones'
    })

def create_region(request):
    if request.method == 'POST':
        formulario = FormRegion(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            name = data_form.get('name')
            cases = data_form['cases']
            deaths = data_form['deaths']
            lethality = data_form['lethality']
            
            region = Region(
                name = name,
                cases = cases,
                deaths = deaths,
                lethality = lethality
            )
            region.save()

            #Es para crear un mensaje Flash (Solo se muestra una vez)
            messages.success(request,f'Se agregó correctamente la region {region.id}')

            return redirect('region')
            #return HttpResponse(articulo.titulo + ' - ' + articulo.contenido + ' - ' + str(articulo.publicado))
    else:
        formulario = FormRegion()        
    return render(request, 'create_region.html',{
        'form': formulario
    })

def empleado(request):
    empleados = Empleado.objects.all()
   
    return render(request, 'empleado.html',{
        'empleados': empleados,
        'titulo': 'Listado de Empleados'
    })

def create_empleado(request):
    if request.method == 'POST':
        formulario = FormEmpleado(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            fullname = data_form.get('fullname')
            job = data_form['job']
            state = data_form['state']
            empleado = Empleado(
                fullname = fullname,
                job = job,
                state = state
            )
            empleado.save()

            #Es para crear un mensaje Flash (Solo se muestra una vez)
            messages.success(request,f'Se agregó correctamente el artículo {empleado.id}')

            return redirect('empleado')
            #return HttpResponse(articulo.titulo + ' - ' + articulo.contenido + ' - ' + str(articulo.publicado))
    else:
        formulario = FormEmpleado()        
    return render(request, 'create_empleado.html',{
        'form': formulario
    })

def save_region(request):
    if request.method == 'POST':
        name = request.POST['name']
        if len(titulo)<=5:
            return HttpResponse("<h2>El tamaño del título es pequeño, intente nuevamente</h2>")
        cases = request.POST['cases']
        deaths = request.POST['deaths']
        lethality = request.POST['lethality']
        

        region = Region(
            name = name,
            cases = cases,
            deaths = deaths,
            lethality = lethality
        )
        region.save()
        return HttpResponse(f"Region Creado: {region.name} ")
    else:
        return HttpResponse("<h2> No se ha podido registrar la region </h2>")


def save_empleado(request):
    if request.method == 'POST':
        fullname = request.POST['fullname']
        if len(titulo)<=5:
            return HttpResponse("<h2>El tamaño del título es pequeño, intente nuevamente</h2>")
        job = request.POST['job']
        state = request.POST['state']

        empleado = Empleado(
            fullname = fullname,
            job = job,
            state = state
        )
        empleado.save()
        return HttpResponse(f"Empleado Creado: {empleado.fullname} ")
    else:
        return HttpResponse("<h2> No se ha podido registrar el empleado </h2>")

def eliminar_region(request, id):
    region = Region.objects.get(pk=id)
    region.delete()
    return redirect('region')

def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(pk=id)
    empleado.delete()
    return redirect('empleado')


    