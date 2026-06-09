# tests/test_calculadora.py
import scr.calculadora

def test_sumar_dos_numeros():
    assert scr.calculadora.sumar(2, 3) == 5

def test_restar():
    assert scr.calculadora.restar(5, 3) == 2
    
def test_multiplicar():
    assert scr.calculadora.multiplicar(4, 2) == 8
