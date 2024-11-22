def juntar_listas(lista1, lista2):

  conjunto = set(lista1) | set(lista2)
  lista_final = list(conjunto)

  return lista_final


lista_1 = [1, 2, 3, 4]
lista_2 = [3, 4, 5, 6]
print(juntar_listas(lista_1, lista_2)) 