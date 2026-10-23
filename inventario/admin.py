
from django.contrib import admin
from .models import Producto, RegistroAuditoria, MovimientoBodega


# ==========================================
# ADMINISTRACIÓN DE PRODUCTOS
# ==========================================

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "codigo",
        "nombre",
        "grupo",
        "unidad_medida",
        "cantidad",
        "precio",
    )
    search_fields = (
        "codigo",
        "nombre",
        "codigo_barras",
    )
    list_filter = ("grupo", "unidad_medida")


# ==========================================
# REGISTRO DE AUDITORÍA
# ==========================================

@admin.register(RegistroAuditoria)
class RegistroAuditoriaAdmin(admin.ModelAdmin):
    list_display = (
        "fecha",
        "usuario",
        "accion",
        "producto_codigo",
    )
    search_fields = (
        "producto_codigo",
        "detalle",
        "usuario__username",
    )
    list_filter = ("accion", "fecha")
    readonly_fields = (
        "usuario",
        "accion",
        "producto_codigo",
        "detalle",
        "fecha",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


# ==========================================
# MOVIMIENTOS DE BODEGA
# ==========================================

@admin.register(MovimientoBodega)
class MovimientoBodegaAdmin(admin.ModelAdmin):
    list_display = (
        "fecha",
        "producto",
        "tipo",
        "cantidad",
        "usuario",
    )
    list_filter = ("tipo", "fecha")
    search_fields = (
        "producto__codigo",
        "producto__nombre",
        "usuario__username",
    )
    readonly_fields = (
        "producto",
        "usuario",
        "tipo",
        "cantidad",
        "observacion",
        "fecha",
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False