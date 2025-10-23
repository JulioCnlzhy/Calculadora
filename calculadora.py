# calculadora.py

def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números. Lanza una excepción si b es 0."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b
