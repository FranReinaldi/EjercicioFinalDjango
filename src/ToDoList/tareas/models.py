from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.http import HttpResponse, JsonResponse

class Tarea(models.Model):
    
    STATUS_CHOICES = (
        ('To Do', 'To Do'),
        ('In Progress','In Progress'),
        ('Done','Done'),
        ('Close','Close'),
        
    )
    name = models.CharField('Nombre', max_length=30)
    description = models.TextField('Descripción', max_length=50)
    comments = models.TextField('Comentarios', max_length=250, null=True)
    status = models.CharField('Estado',max_length=20, choices=STATUS_CHOICES,
                                default='To Do')
    date_create = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    expire_date = models.DateTimeField('Fecha de vencimiento', null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    @property
    def is_past_due(self):
        """
        permite calcular si la tarea esta vencida o no
        """
        return datetime.today() > self.expire_date.replace(tzinfo=None)
    

