from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.db.models import Q
from .forms import NewUserForm
from django.contrib.auth import login
import datetime

from .forms import CreationForm
from .forms import EditForm

from .models import Tarea

@login_required
def get_tareas(request):
    
    #lista todas las tareas del usuario
    
    tareas = Tarea.objects.all()
    busqueda = request.GET.get("buscar")
    if busqueda:
        tareas = Tarea.objects.filter(
            Q(name__icontains = busqueda)|
            Q(description__icontains = busqueda)|
            Q(status__icontains = busqueda)
        ).distinct()
    form = CreationForm()
    error = False
    if request.method == 'POST':
        form = CreationForm(request.POST)
        form.instance.user= request.user
        if form.is_valid():
            form.save(commit=True)
        else:
            error = True
    return render(request, 'tareas/tarea_list.html',
                  context={'tareas': tareas,
                           'error': error,
                           'form': form})

@login_required

def tarea(request, id_tarea):
    
    #muestra una tarea en especifico
    
    tarea = Tarea.objects.get(pk=id_tarea)
    form = EditForm(instance=tarea)
    if request.method == 'POST':
        form = EditForm(request.POST, instance=tarea)
        if form.is_valid():
            form.save(commit=True)
    return render(request, 'tareas/tarea_detail.html',
                      context = {'tarea': tarea,
                                 'form':form})


def eliminar_tarea(request, id_tarea):
    """
    permite eliminar una tarea
    """
    try:
        tarea = Tarea.objects.get(pk=id_tarea)
    except Tarea.DoesNotExist:
        return redirect("../")

    if tarea.user != request.user:
        return redirect("../")
    else:
        tarea.delete()
        return redirect("../")

def register_request(request):
    
    #permite registrar nuevos usuarios
    
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect("/")
	form = NewUserForm()
	return render (request=request, template_name="tareas/register.html", context={"register_form":form})

