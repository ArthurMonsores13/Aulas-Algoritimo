def numeros_primos_ate(n):

  primos = [True] * (n+1)
  p = 2

  while (p * p <= n):
    if (primos[p] == True):
      for i in range(p * p, n+1, p):
        primos[i] = False
    p += 1

  resultado = []
  for p in range(2, n+1):
    if primos[p]:
      resultado.append(p)
  
  return resultado

print(numeros_primos_ate(20))