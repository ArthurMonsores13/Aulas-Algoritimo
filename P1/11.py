''' Dada uma lista de números, escreva um código que crie uma nova lista contendo apenas os números que são múltiplos de 3 ou 5. 
'''
lista =  []
multiplos = []
while True:
    num = int(input("Digite os números ou 0 para  sair: "))
    
    if num == 0:
        break
    else:
        lista.append(num)
    
for num in lista:
    if num % 3 == 0 or num % 5 == 0: 
        multiplos.append(num)
    else:
        continue
        
print(multiplos)
    