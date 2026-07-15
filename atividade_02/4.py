def segundo_maior(lista):
    unicos = list(set(lista))
    unicos.sort(reverse=True)
    return unicos[1] if len(unicos) > 1 else None

print(segundo_maior([10, 5, 8, 20, 20, 3]))  # 10