def soma_lista(lista):
    total = 0
    for item in lista:
        if isinstance(item, list):  # Se o item for uma lista, chama recursivamente
            total += soma_lista(item)
        else:
            total += item  # Se for um número, adiciona diretamente ao total
    return total

# Exemplo de uso:
lista = [5, [2, 3], 10]
print(soma_lista(lista))  # Saída: 10
