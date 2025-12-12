from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import BusquedaProductoForm, ProductoForm
from django.views.decorators.http import require_POST

def lista_productos(request):
    # queryset base
    productos = Producto.objects.select_related('categoria').all()

    # formulario de búsqueda (lee request.GET)
    form = BusquedaProductoForm(request.GET or None)

    if form.is_valid():
        q = form.cleaned_data.get('q')
        categoria = form.cleaned_data.get('categoria')

        if q:
            productos = productos.filter(nombre__icontains=q)

        if categoria:
            productos = productos.filter(categoria=categoria)

    contexto = {
        'productos': productos,
        'form': form,
    }
    return render(request, 'catalogo/lista_productos.html', contexto)

def detalle_producto(request, pk):
    producto = get_object_or_404(
        Producto.objects.select_related('categoria'),
        pk=pk
    )

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            # después de guardar, recargo la misma página
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm(instance=producto)

    contexto = {
        'producto': producto,
        'form': form,
    }
    return render(request, 'catalogo/detalle_producto.html', contexto)


def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            return redirect('detalle_producto', pk=producto.pk)
    else:
        form = ProductoForm()

    contexto = {
        'form': form,
    }
    return render(request, 'catalogo/crear_producto.html', contexto)

@require_POST
def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    producto.delete()
    return redirect('lista_productos')
