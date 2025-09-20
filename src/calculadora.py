def somar(a, b):
    return a + b

def dividir(a, b):
    if b == 0:
        raise ValueError("Divisão por zero!")
    return a / b

def multiplicacao(a, b):
    if b == 0:
        raise ValueError("O valor é zero!")
    return a * b

def subtracao(a, b):
    return a - b
#