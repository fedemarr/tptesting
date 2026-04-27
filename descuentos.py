def calcular_descuento(precio: float, porcentaje: float) -> float:
    if precio < 0:
        raise ValueError("El precio no puede ser negativo.")
    if not (0 <= porcentaje <= 100):
        raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
    descuento = precio * (porcentaje / 100)
    return round(precio - descuento, 2)


def aplicar_descuento_por_categoria(precio: float, categoria: str) -> float:
    descuentos_por_categoria = {
        "electronica": 15,
        "ropa": 10,
        "alimentos": 5,
    }
    porcentaje = descuentos_por_categoria.get(categoria.lower(), 0)
    return calcular_descuento(precio, porcentaje)


def calcular_descuento_acumulado(precio: float, porcentajes: list) -> float:
    precio_actual = precio
    for p in porcentajes:
        precio_actual = calcular_descuento(precio_actual, p)
    return precio_actual
