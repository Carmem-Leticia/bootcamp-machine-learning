def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def numeros_primos(lista):
    return [n for n in lista if eh_primo(n)]

print(numeros_primos([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  