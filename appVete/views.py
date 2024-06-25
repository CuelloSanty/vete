from django.shortcuts import render, get_object_or_404
from .models import Articulo, Proveedore
# Create your views here.


def index(request):
    return render(request,"index.html")

def article(request):
    item = Articulo.objects.all()
    return render(request,"Articulo.html",{"item":item})

def art_detail(request,pk):
    item = Articulo.objects.get(pk=pk)
    return render(request, "Articulo_detalle.html",{"item":item})

def form(request):

    if request.method == "GET": 
        return render(request,'forms/formulario_Articulo.html',
        {"tom": Proveedore.objects.all()}) 
    else:
        try:
            Articulo.objects.create(
                codigo=request.POST["codigo"],
                nombre=request.POST["nombre"],
                descripcion=request.POST["descripcion"],
                img=request.POST["img"],
                marca=request.POST["marca"],
                peso=request.POST["peso"],
                talle=request.POST["talle"],
                vencimiento=request.POST["vencimiento"],
                unidad=request.POST["unidad"],
                cantidad=request.POST["cantidad"],
                precio=request.POST["precio"],
                tipo=request.POST["tipo"],
                proveedor=get_object_or_404(Proveedore, pk=request.POST.get("proveedor"))
                )
            return render(request, "state_form/succes.html")
        except Exception:
            return render(request, "state_form/wrong.html")
        


    

    