from django.db import models
from django.urls import reverse

class Producto(models.Model):
    titulo      = models.CharField(max_length=120) # obligatorio añadir max_length
    descripcion = models.TextField(blank=True, null=True)
    precio      = models.DecimalField(decimal_places=2, max_digits=10000) # buscar en docs por un field de decimiles
    resumen     = models.TextField(blank=False, null=False)
    destacado   = models.BooleanField(default=False)

    def get_absolute_url(self):
        #return f"/product/{self.id}"
        return reverse("productos:product-detail", kwargs={"id": self.id})