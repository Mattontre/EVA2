from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Producto, RegistroAuditoria, MovimientoBodega
from .forms import ProductoForm, MovimientoBodegaForm


def es_administrador_inventario(user):
    return (
        user.is_authenticated
        and user.groups.filter(
            name="AdministradoresInventario"
        ).exists()
    )


def registrar_auditoria(usuario, accion, codigo, detalle=""):
    RegistroAuditoria.objects.create(
        usuario=usuario,
        accion=accion,
        producto_codigo=codigo,
        detalle=detalle,
    )


@login_required
def lista_productos(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(
        request,
        "inventario/lista_productos.html",
        {"productos": productos},
    )


@login_required
@user_passes_test(es_administrador_inventario)
def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                producto = form.save()
                registrar_auditoria(
                    request.user,
                    "CREAR",
                    producto.codigo,
                    f"Se creó el producto: {producto.nombre}",
                )
            messages.success(request, "Producto creado correctamente.")
            return redirect("lista_productos")
    else:
        form = ProductoForm()

    return render(
        request,
        "inventario/crear_producto.html",
        {"form": form},
    )


@login_required
@user_passes_test(es_administrador_inventario)
def editar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == "POST":
        codigo_anterior = producto.codigo
        nombre_anterior = producto.nombre
        form = ProductoForm(request.POST, instance=producto)

        if form.is_valid():
            with transaction.atomic():
                producto = form.save()
                registrar_auditoria(
                    request.user,
                    "EDITAR",
                    producto.codigo,
                    (
                        f"Antes: {codigo_anterior} - {nombre_anterior}. "
                        f"Después: {producto.codigo} - {producto.nombre}."
                    ),
                )
            messages.success(request, "Producto actualizado correctamente.")
            return redirect("lista_productos")
    else:
        form = ProductoForm(instance=producto)

    return render(
        request,
        "inventario/editar_producto.html",
        {"form": form, "producto": producto},
    )


@login_required
@user_passes_test(es_administrador_inventario)
def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)

    if request.method == "POST":
        with transaction.atomic():
            registrar_auditoria(
                request.user,
                "ELIMINAR",
                producto.codigo,
                f"Se eliminó el producto: {producto.nombre}",
            )
            producto.delete()

        messages.success(request, "Producto eliminado correctamente.")
        return redirect("lista_productos")

    return render(
        request,
        "inventario/confirmar_eliminacion.html",
        {"producto": producto},
    )


# ==========================================
# MOVIMIENTOS DE BODEGA
# ==========================================

@login_required
def lista_movimientos(request):
    movimientos = MovimientoBodega.objects.select_related(
        "producto", "usuario"
    ).order_by("-fecha")

    return render(
        request,
        "inventario/lista_movimientos.html",
        {"movimientos": movimientos},
    )


@login_required
@user_passes_test(es_administrador_inventario)
def crear_movimiento(request):
    if request.method == "POST":
        form = MovimientoBodegaForm(request.POST)

        if form.is_valid():
            producto_id = form.cleaned_data["producto"].id
            tipo = form.cleaned_data["tipo"]
            cantidad = form.cleaned_data["cantidad"]
            observacion = form.cleaned_data["observacion"]

            with transaction.atomic():
                producto = get_object_or_404(
                    Producto.objects.select_for_update(),
                    id=producto_id,
                )

                if tipo == "SALIDA" and cantidad > producto.cantidad:
                    form.add_error(
                        "cantidad",
                        "No hay suficiente stock para esta salida.",
                    )
                else:
                    if tipo == "ENTRADA":
                        producto.cantidad += cantidad
                    else:
                        producto.cantidad -= cantidad

                    producto.save(update_fields=["cantidad"])

                    movimiento = form.save(commit=False)
                    movimiento.producto = producto
                    movimiento.usuario = request.user
                    movimiento.observacion = observacion
                    movimiento.save()

                    registrar_auditoria(
                        request.user,
                        "MOVIMIENTO",
                        producto.codigo,
                        (
                            f"{tipo}: {cantidad} unidades. "
                            f"Stock resultante: {producto.cantidad}. "
                            f"Observación: {observacion}"
                        ),
                    )

                    messages.success(
                        request,
                        f"Movimiento registrado. Stock actual: "
                        f"{producto.cantidad}.",
                    )
                    return redirect("lista_movimientos")
    else:
        form = MovimientoBodegaForm()

    return render(
        request,
        "inventario/crear_movimiento.html",
        {"form": form},
    )