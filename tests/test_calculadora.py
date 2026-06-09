# tests/test_calculadora.py
from src import calculadora

def test_sumar_dos_numeros():
    assert calculadora.sumar(2, 3) == 5

def test_restar():
    assert calculadora.restar(5, 3) == 2
    
def test_multiplicar():
    assert calculadora.multiplicar(4, 2) == 8
