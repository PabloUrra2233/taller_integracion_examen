from django.shortcuts import render
from .models import Producto
from .forms import BusquedaProductoForm


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
