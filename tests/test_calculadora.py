# tests/test_calculadora.py
import pytest
from src.calculadora import somar, dividir, multiplicacao, subtracao

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    with pytest.raises(ValueError):
        dividir(10, 0)

def test_multiplicacao():
    assert multiplicacao(2, 3) == 6
    assert multiplicacao(0, 5) == 0

def test_subtracao():
    assert subtracao(10, 2) == 8
    assert subtracao(4, 1) == 3
