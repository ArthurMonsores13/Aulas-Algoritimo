def rodar_lista(lista, k):
    k = k % len(lista)  #
    return lista[-k:] + lista[:-k]  # Combina os últimos k elementos com o restante


lista = [10,11,12,13,14]
k = 2
print(rodar_lista(lista, k))  
