def ordenar_por_nome(pessoas):
    return sorted(pessoas, key=lambda pessoa: pessoa[0])

pessoas = [("Eric", 30), ("Ana", 25), ("Diogo", 22)]
print(ordenar_por_nome(pessoas))
# [('Ana', 25), ('Diogo', 22), ('Eric', 30)]