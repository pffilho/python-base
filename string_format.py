#!/usr/bin/env python3
"""Imprime a tabudada do 1 ao 10
---Tabuada do 1---
1 x 1 = 1
2 x 1 = 2
3 x 1 = 3
...
##################
---Tabuada do 2---
1 x 2 = 2
2 x 2 = 4
3 x 2 = 6
...
"""
__version__ = "0.1.1"
__author__ = "pfranco"

template_base = """
---Tabuada do {num}---
{bloco:^18}    
##################
"""

# numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros = list(range(1, 11))

# Iterable (percorriveis)
"""
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print('------------')
"""

for n1 in numeros:
    print("{:^18}".format(f"Tabuada do {n1}"))
    print()
    
    for n2 in numeros:
        # operacao = f"{n1} x {n2} = {n1 * n2}"
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    
    print("#" * 18)