from django.shortcuts import render
from .models import Web

# Create your views here.

def conocimientosweb(request):
    webs = Web.objects.all()
    return render(request, 'web/conocimientosweb.html',{'webs':webs})