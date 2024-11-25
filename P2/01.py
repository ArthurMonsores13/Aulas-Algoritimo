def numeros_primos(lista):
    return [n for n in lista if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))]


lista = [20,323,130,1,3,5,9]
print(numeros_primos(lista))  
