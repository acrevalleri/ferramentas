import sys

def soma(x, y):
    return x+y

def subtracao(x, y):
    return x-y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y != 0:
        return x/y
    else:
        print("jamais dividiras por zero")

try:
    nmr1 = float(sys.argv[1])
    op = str(sys.argv[2])
    nmr2 = float(sys.argv[3])
except:
    print("usage:python3 calculadora.py nmr1 operador nmr2 (ex: 15 / 5)")


if op == "+":
    resultado = soma(nmr1, nmr2)
elif op == "-":
    resultado = subtracao(nmr1, nmr2)
elif op == "*":
    resultado = multiplicacao(nmr1, nmr2)
elif op == "/":
    resultado = divisao(nmr1, nmr2)

print(resultado)
