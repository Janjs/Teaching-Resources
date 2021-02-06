"""primerproyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import (
    producto_detalle_view,
    producto_create_view,
    producto_modify_view,
    producto_detalle_dynamic_view,
    producto_delete_view,
    ProductoListView
)

app_name = 'productos'
urlpatterns = [
    path('<int:id>/', producto_detalle_dynamic_view, name="product-detail"),
    path('<int:id>/delete', producto_delete_view, name="product-delete"),
    path('create/', producto_create_view),
    path('modify/', producto_modify_view),
    path('', ProductoListView.as_view(), name="product-list"),
]
