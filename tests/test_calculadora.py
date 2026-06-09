# tests/test_calculadora.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src import calculadora

def test_sumar_dos_numeros():
    assert calculadora.sumar(2, 3) == 5

def test_restar():
    assert calculadora.restar(5, 3) == 2
    
def test_multiplicar():
    assert calculadora.multiplicar(4, 2) == 8
