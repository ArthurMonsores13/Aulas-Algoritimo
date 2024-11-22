def ordenar_lista(lista):
  n = len(lista)
  
  for i in range(n):
    
    for j in range(0, n-i-1):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
  return lista

minha_lista = [2, 4, 6, 12, 16, 5, 8, 9, 18]
print(ordenar_lista(minha_lista))