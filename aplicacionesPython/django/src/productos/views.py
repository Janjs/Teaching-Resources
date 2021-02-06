from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Producto
from .forms import ProductoForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    ListView,
    DeleteView
)

class ProductoListView(ListView):
    template_name = 'producto/producto_list.html'
    queryset = Producto.objects.all() #<productos>/<modelname>_list.html

# def producto_list_view(request):
#     queryset = Producto.objects.all() # lista de objetos
#     contexto = {
#         'object_list': queryset
#     }
#     return render(request, "producto/producto_list.html", contexto)

def producto_delete_view(request, id):
    obj = get_object_or_404(Producto, id=id)
    #POST request, también se usa DELETE
    if request.method == "POST":
        # confirmamos
        obj.delete()
        return redirect("../../")
    contexto = {
        'producto': obj
    }
    return render(request, "producto/producto_delete.html", contexto)


def producto_detalle_dynamic_view(request, id):
    #obj = Producto.objects.get(id=id)
    #obj = get_object_or_404(Producto, id=id)
    try:
        obj = Producto.objects.get(id=id)
    except Producto.DoesNotExist:
        raise Http404
    contexto = {
        'producto': obj
    }
    return render(request, "producto/producto_detalle.html", contexto)

def producto_detalle_view(request):
    obj = Producto.objects.get(id=1)
    contexto = {
        'producto': obj
    }
    return render(request, "producto/producto_detalle.html", contexto)

def producto_detalle_view(request):
    obj = Producto.objects.get(id=1)
    contexto = {
        'producto': obj
    }
    return render(request, "producto/producto_detalle.html", contexto)

def producto_create_view(request):
    initial_data = {
        'titulo': "Producto x"
    }

    form = ProductoForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = ProductoForm()

    contexto = {
        'form': form
    }
    return render(request, "producto/producto_crear.html", contexto)

def producto_modify_view(request):
    obj = Producto.objects.get(id=1)
    form = ProductoForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        form = ProductoForm()

    contexto = {
        'form': form
    }
    return render(request, "producto/producto_crear.html", contexto)


# def producto_create_view(request):
#     mi_nuevo_titulo = request.POST.get('titulo')
#     print(mi_nuevo_titulo)
#     contexto = {}
#     return render(request, "producto/producto_crear.html", contexto)

# def producto_create_view(request):
#     mi_form = PuroProductoForm()
#     if request.method == "POST":
#         mi_form = PuroProductoForm(request.POST)
#         if mi_form.is_valid():
#             print(mi_form.cleaned_data)
#             Producto.objects.create(**mi_form.cleaned_data)
#         else:
#             print(mi_form.errors)
#     contexto = {
#         "form": mi_form
#     }
#     return render(request, "producto/producto_crear.html", contexto)
#
