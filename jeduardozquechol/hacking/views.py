from django.shortcuts import render
from .models import Hacking

# Create your views here.
def conocimientoshacking(request):
    hacks = Hacking.objects.all()
    
    return render(request, 'hacking/conocimientoshacking.html',{'hacks':hacks})

