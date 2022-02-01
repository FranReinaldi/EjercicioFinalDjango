from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import tarea, get_tareas, eliminar_tarea
from . import views


urlpatterns = [
    path('<int:id_tarea>', tarea),
    path('', get_tareas),
    path('delete/<id_tarea>', eliminar_tarea),
    path("register", views.register_request, name="register")
    
    
]
