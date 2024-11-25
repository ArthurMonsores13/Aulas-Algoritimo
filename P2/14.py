def intersecao(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Exemplo de uso:
lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]
print(intersecao(lista1, lista2))  # Saída: [4, 5]
