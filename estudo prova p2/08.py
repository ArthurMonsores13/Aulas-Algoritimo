def ordenar_lista(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista

print(ordenar_lista([5, 3, 8, 4, 2])) 
