from django.shortcuts import render, redirect, get_object_or_404
from .models import Seccion
from .forms import SeccionForm

def lista_secciones(request):
    seccion = Seccion.objects.filter(activo=True)
    return render(request, "secciones/secciones.html", {"secciones": seccion})

def nuevo_seccion(request):
    form = SeccionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("secciones")
    return render(request, "shared/form.html", {
        "form": form,
        "titulo_formulario": "Nueva Seccion",
        "url_lista": "/secciones/"
    })

def editar_seccion(request, id):
    seccion = get_object_or_404(Seccion, id=id)
    form = SeccionForm(request.POST or None, instance=seccion)
    if form.is_valid():
        form.save()
        return redirect("secciones")
    return render(request, "shared/form.html", {
        "form": form,
        "titulo_formulario": f"Editar Seccion #{seccion.id}",
        "url_lista": "/productos/"
    })

def anular_seccion(request, id):
    seccion = get_object_or_404(Seccion, id=id)
    seccion.activo = False
    seccion.save()
    return redirect("secciones")
