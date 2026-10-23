from django import forms
from .models import Producto, MovimientoBodega


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
            "codigo",
            "nombre",
            "codigo_barras",
            "grupo",
            "subgrupo",
            "ficha_tecnica",
            "unidad_medida",
            "cantidad",
            "precio",
        ]

    def clean_codigo(self):
        codigo = self.cleaned_data["codigo"].strip()
        if not codigo:
            raise forms.ValidationError(
                "El código es obligatorio."
            )
        return codigo

    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"].strip()
        if not nombre:
            raise forms.ValidationError(
                "El nombre es obligatorio."
            )
        return nombre

    def clean_cantidad(self):
        cantidad = self.cleaned_data["cantidad"]
        if cantidad < 0:
            raise forms.ValidationError(
                "La cantidad no puede ser negativa."
            )
        return cantidad

    def clean_precio(self):
        precio = self.cleaned_data["precio"]
        if precio < 0:
            raise forms.ValidationError(
                "El precio no puede ser negativo."
            )
        return precio


class MovimientoBodegaForm(forms.ModelForm):
    class Meta:
        model = MovimientoBodega
        fields = ["producto", "tipo", "cantidad", "observacion"]
        widgets = {
            "observacion": forms.Textarea(
                attrs={"rows": 3}
            ),
        }

    def clean_cantidad(self):
        cantidad = self.cleaned_data["cantidad"]

        if cantidad <= 0:
            raise forms.ValidationError(
                "La cantidad debe ser mayor que cero."
            )

        return cantidad

    def clean_observacion(self):
        observacion = self.cleaned_data.get("observacion", "")
        return observacion.strip()