# ============================================
# SISTEMA DE VENTAS
# ============================================

def calcular_subtotal(precios, cantidades):
    subtotal = 0

    # [CORREGIDO] Antes tenía range(len(precios) - 1), dejando fuera el último producto
    for i in range(len(precios)):
        subtotal = subtotal + precios[i] * cantidades[i]

    return subtotal


def calcular_descuento(subtotal):
    descuento = 0

    # [CORREGIDO] Se evalúa primero > 1000; antes > 500 capturaba todos los casos mayores a 1000
    if subtotal > 1000:
        descuento = subtotal * 0.20
    elif subtotal > 500:
        descuento = subtotal * 0.10

    return descuento


def calcular_iva(total):
    iva = total * 0.10
    return iva


def producto_mas_caro(productos, precios):
    # [CORREGIDO] Validar lista vacía
    if len(productos) == 0:
        return "Ninguno", 0

    mayor = precios[0]
    nombre = productos[0]

    for i in range(len(productos)):
        # [CORREGIDO] Antes usaba '<', buscando el más barato en lugar del más caro
        if precios[i] > mayor:
            mayor = precios[i]
            nombre = productos[i]

    return nombre, mayor


def contar_productos_descuento(precios):
    contador = 0

    for precio in precios:
        if precio > 500:
            contador = contador + 1

    return contador


def mostrar_factura(productos, precios, cantidades):
    subtotal = calcular_subtotal(precios, cantidades)
    descuento = calcular_descuento(subtotal)

    # [CORREGIDO] El descuento se RESTA al subtotal; antes lo sumaba (subtotal + descuento)
    total_con_descuento = subtotal - descuento

    iva = calcular_iva(total_con_descuento)
    total = total_con_descuento + iva

    producto_caro, precio_caro = producto_mas_caro(productos, precios)
    cantidad_descuento = contar_productos_descuento(precios)

    print("\n========== FACTURA ==========")

    for i in range(len(productos)):
        importe = precios[i] * cantidades[i]

        print(
            productos[i],
            "Cantidad:", cantidades[i],
            "Precio:", precios[i],
            "Importe:", importe
        )

    print("-----------------------------")
    print("Subtotal:", round(subtotal, 2))
    print("Descuento:", round(descuento, 2))
    print("IVA:", round(iva, 2))
    print("Total:", round(total, 2))
    print("Producto más caro:", producto_caro)
    print("Precio mayor:", precio_caro)
    print("Productos con descuento:", cantidad_descuento)
    print("=============================")


# ============================================
# PROGRAMA PRINCIPAL
# ============================================

productos = []
precios = []
cantidades = []

cantidad = int(input("¿Cuántos productos desea registrar?: "))

for i in range(cantidad):
    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    cantidad_producto = int(input("Ingrese la cantidad: "))

    # [CORREGIDO] Se cambió 'or' por 'and' para exigir precio > 0 Y cantidad > 0
    if precio > 0 and cantidad_producto > 0:
        productos.append(producto)
        precios.append(precio)
        cantidades.append(cantidad_producto)
        print("Producto registrado correctamente.")
    else:
        # [CORREGIDO] Antes imprimía "Producto registrado correctamente" aunque no lo guardara
        print("Error: el precio y la cantidad deben ser mayores a 0.")

mostrar_factura(productos, precios, cantidades)
