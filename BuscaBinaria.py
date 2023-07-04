import numpy as np
import random

def procura(array, numero):
    tamanhoArray = len(array)
    primeiroindice = 0
    ultimoindice = tamanhoArray-1
    indice_meio = (primeiroindice + ultimoindice)//2
    elemento_do_meio = array[indice_meio]
    while True:
        if primeiroindice == ultimoindice:
            if elemento_do_meio != numero:
                return f'{numero} não está no array'
        if numero == elemento_do_meio:
            return f'posição no array: {indice_meio}'

        elif numero>elemento_do_meio:
            novoindice = indice_meio + 1
            primeiroindice = novoindice
            ultimoindice = tamanhoArray - 1
            indice_meio = (primeiroindice + ultimoindice)//2
            elemento_do_meio = array[indice_meio]
            if numero == elemento_do_meio:
               return f'posição no array: {indice_meio}'

        elif numero<elemento_do_meio:
            novoindice = indice_meio - 1
            ultimoindice = novoindice
            indice_meio = (primeiroindice + ultimoindice)//2
            elemento_do_meio = array[indice_meio]
            if numero == elemento_do_meio:
                return f'posição no array: {indice_meio}'

array = np.arange(0,101)
numero = random.randint(0,101)
print(numero)
print(procura(array, numero))