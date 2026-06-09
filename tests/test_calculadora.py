# tests/test_calculadora.py
import scr.calculadora

def test_sumar_dos_numeros():
    assert src.calculadora.sumar(2, 3) == 5

def test_restar():
    assert src.calculadora.restar(5, 3) == 2
    
def test_multiplicar():
    assert src.calculadora.multiplicar(4, 2) == 8
