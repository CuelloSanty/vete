from django.shortcuts import render
from .models import Articulo
# Create your views here.


def index(request):
    return render(request,"index.html")

def article(request):
    item = Articulo.objects.all()
    return render(request,"Articulo.html",{"item":item})

def art_detail(request,pk):
    item = Articulo.objects.get(pk=pk)
    return render(request, "Articulo_detalle.html",{"item":item})
    