from django import forms
from .models import Producto

class ProductoForm(forms.ModelForm):
    titulo = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    descripcion = forms.CharField(required=False,
                                  widget=forms.Textarea(
                                      attrs={
                                          "class": "nueva-class-nombre dos",
                                          "id": "mi-id-para-text-area",
                                          "cols": 100
                                      }
                                  )
                                  )
    precio = forms.DecimalField(initial=199.99)
    class Meta:
        model = Producto
        fields = [
            'titulo',
            'descripcion',
            'precio'
        ]

    def clean_titulo(self, *args, **kwargs):
        titulo = self.cleaned_data.get("titulo")
        if not "Producto" in titulo:
            raise forms.ValidationError("No contiene la palabra Producto, no es valido")
        else:
            return titulo

# class PuroProductoForm(forms.Form):
#     titulo      = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
#     descripcion = forms.CharField(required=False,
#                                   widget=forms.Textarea(
#                                       attrs={
#                                           "class": "nueva-class-nombre dos",
#                                           "id": "mi-id-para-text-area",
#                                           "cols": 100
#                                       }
#                                   )
#                                   )
#     precio       = forms.DecimalField(initial=199.99)
