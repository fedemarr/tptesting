import pytest
from descuentos import (
    calcular_descuento,
    aplicar_descuento_por_categoria,
    calcular_descuento_acumulado,
)

# CASOS EXITOSOS
def test_descuento_simple_exitoso():
    assert calcular_descuento(1000.0, 20) == 800.0

def test_descuento_cero_por_ciento():
    assert calcular_descuento(500.0, 0) == 500.0

def test_descuento_cien_por_ciento():
    assert calcular_descuento(200.0, 100) == 0.0

def test_descuento_por_categoria_electronica():
    assert aplicar_descuento_por_categoria(10000.0, "electronica") == 8500.0

def test_descuento_por_categoria_ropa():
    assert aplicar_descuento_por_categoria(200.0, "ropa") == 180.0

def test_descuento_por_categoria_alimentos():
    assert aplicar_descuento_por_categoria(100.0, "alimentos") == 95.0

def test_descuento_acumulado_dos_descuentos():
    assert calcular_descuento_acumulado(1000.0, [10, 5]) == 855.0

def test_descuento_categoria_mayusculas():
    assert aplicar_descuento_por_categoria(1000.0, "ELECTRONICA") == 850.0

# CASOS DE ERROR
def test_precio_negativo_lanza_excepcion():
    with pytest.raises(ValueError, match="precio no puede ser negativo"):
        calcular_descuento(-100.0, 10)

def test_porcentaje_mayor_100_lanza_excepcion():
    with pytest.raises(ValueError, match="entre 0 y 100"):
        calcular_descuento(500.0, 150)

def test_porcentaje_negativo_lanza_excepcion():
    with pytest.raises(ValueError, match="entre 0 y 100"):
        calcular_descuento(500.0, -10)

# CASOS BORDE
def test_precio_cero():
    assert calcular_descuento(0.0, 50) == 0.0

def test_descuento_fraccionario():
    assert calcular_descuento(100.0, 33.33) == 66.67

def test_categoria_desconocida_sin_descuento():
    assert aplicar_descuento_por_categoria(1000.0, "juguetes") == 1000.0

def test_lista_descuentos_vacia():
    assert calcular_descuento_acumulado(500.0, []) == 500.0

def test_precio_muy_pequeno():
    assert calcular_descuento(0.10, 10) == 0.09
