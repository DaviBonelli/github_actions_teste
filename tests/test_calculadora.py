# tests/test_calculadora.py
import pytest
from src.calculadora import somar, dividir, multiplicacao, subtrair

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_multiplicacao():
    assert multiplicar(2, 3) == 6
    with pytest.raises(ValueError):
        multiplicar(0, 5) == 0

def test_subtracao():
    assert subtrair(10, 2) == 8
    assert subtrair(4, 1) == 3
