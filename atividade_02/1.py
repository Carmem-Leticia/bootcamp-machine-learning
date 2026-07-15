def numeros_impares(lista):
    return [n for n in lista if n % 2 != 0]

print(numeros_impares([1, 2, 3, 4, 5, 6]))  # [1, 3, 5]