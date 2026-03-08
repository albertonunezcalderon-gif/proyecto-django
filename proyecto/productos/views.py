from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import ProductoForm

def lista_productos(request):
    # Tomamos los parámetros del GET
    nombre = request.GET.get('nombre', '')
    categoria = request.GET.get('categoria', '')
    stock = request.GET.get('stock', '')
    precio_min = request.GET.get('precio_min', '')
    precio_max = request.GET.get('precio_max', '')

    productos = Producto.objects.all()

    # Filtramos según los parámetros si existen
    if nombre:
        productos = productos.filter(nombre__icontains=nombre)
    if categoria:
        productos = productos.filter(seccion__nombre__icontains=categoria)
    if stock:
        try:
            productos = productos.filter(stock__gte=int(stock))
        except ValueError:
            pass
    if precio_min:
        try:
            productos = productos.filter(precio__gte=float(precio_min))
        except ValueError:
            pass
    if precio_max:
        try:
            productos = productos.filter(precio__lte=float(precio_max))
        except ValueError:
            pass

    return render(request, "productos/productos.html", {
        "productos": productos,
        "filtros": {
            "nombre": nombre,
            "categoria": categoria,
            "stock": stock,
            "precio_min": precio_min,
            "precio_max": precio_max
        }
    })

def nuevo_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("productos")
    return render(request, "shared/form.html", {
        "form": form,
        "titulo_formulario": "Nuevo Producto",
        "url_lista": "/productos/"
    })

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect("productos")
    return render(request, "shared/form.html", {
        "form": form,
        "titulo_formulario": f"Editar Producto #{producto.id}",
        "url_lista": "/productos/"
    })

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()  # Borra el producto de la base de datos
    return redirect("productos")
