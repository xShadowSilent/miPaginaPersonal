from django.shortcuts import render
from .models import Programacion

# Create your views here.
def conocimientospro(request):
    programaciones = Programacion.objects.all()
    return render(request, 'programacion/conocimientospro.html',{'programaciones':programaciones})
