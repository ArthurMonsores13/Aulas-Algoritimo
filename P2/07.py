def juntar_listas(lista1, lista2):
    i, j = 0, 0
    resulta = []
    
    while i < len(lista1) and j < len(lista2):
        if lista1[i] < lista2[j]:
            resulta.append(lista1[i])
            i += 1
        else:
            resulta.append(lista2[j])
            j += 1
    # Adiciona os elementos restantes de lista1, se houver
    while i < len(lista1):
        resulta.append(lista1[i])
        i += 1
    # Adiciona os elementos restantes de lista2, se houver
    while j < len(lista2):
        resulta.append(lista2[j])
        j += 1
    return resulta

# Exemplo de uso:
lista1 = [1, 3, 5]
lista2 = [2, 4, 6]
print(juntar_listas(lista1, lista2))  # Saída: [1, 2, 3, 4, 5, 6]
