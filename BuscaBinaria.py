import numpy as np
import random

array = np.array([4,12,27,32,36])
tamanhoArray = len(array)
primeiroindice = 0
ultimoindice = tamanhoArray-1
indice_meio = (primeiroindice + ultimoindice)//2
elemento_do_meio = array[indice_meio]
numero = 17
while True:
    if primeiroindice == ultimoindice:
        if elemento_do_meio != numero:
            print("Não aparece na lista")
            break
    if numero == elemento_do_meio:
        print(f"{elemento_do_meio} encontrado na posição {indice_meio}")
        break

    elif numero>elemento_do_meio:
        novoindice = indice_meio + 1
        primeiroindice = novoindice
        ultimoindice = tamanhoArray - 1
        indice_meio = (primeiroindice + ultimoindice)//2
        elemento_do_meio = array[indice_meio]
        if numero == elemento_do_meio:
            print(f"{elemento_do_meio} encontrado na posição {indice_meio}")
            break

    elif numero<elemento_do_meio:
        novoindice = indice_meio - 1
        ultimoindice = novoindice
        indice_meio = (primeiroindice + ultimoindice)//2
        elemento_do_meio = array[indice_meio]
        if numero == elemento_do_meio:
            print(f"{elemento_do_meio} encontrado na posição {indice_meio}")
            break