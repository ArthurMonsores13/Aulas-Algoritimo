def lista_pares(lista):
  pares = []
  for i in lista:
    if i % 2 == 0:
      pares.append(i)
  return pares

print(lista_pares([1, 2, 3, 4, 5, 6, 7, 8]))