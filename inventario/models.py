
from django.conf import settings
from django.db import models


# ==========================================
# PRODUCTOS DEL INVENTARIO
# ==========================================

class Producto(models.Model):
    codigo = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=150)
    codigo_barras = models.CharField(max_length=50, blank=True)
    grupo = models.CharField(max_length=100)
    subgrupo = models.CharField(max_length=100, blank=True)
    ficha_tecnica = models.TextField(blank=True)
    unidad_medida = models.CharField(max_length=30)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"


# ==========================================
# REGISTRO DE AUDITORÍA
# ==========================================

class RegistroAuditoria(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    accion = models.CharField(max_length=20)
    producto_codigo = models.CharField(max_length=20)
    detalle = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.accion} - {self.producto_codigo} "
            f"- {self.fecha}"
        )


# ==========================================
# MOVIMIENTOS DE BODEGA
# ==========================================

class MovimientoBodega(models.Model):
    TIPOS_MOVIMIENTO = [
        ("ENTRADA", "Entrada"),
        ("SALIDA", "Salida"),
    ]

    producto = models.ForeignKey(
        Producto,
        on_delete=models.PROTECT,
        related_name="movimientos",
    )
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    tipo = models.CharField(
        max_length=10,
        choices=TIPOS_MOVIMIENTO,
    )
    cantidad = models.PositiveIntegerField()
    observacion = models.CharField(
        max_length=250,
        blank=True,
    )
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.tipo} - {self.producto.codigo} "
            f"- {self.cantidad}"
        )