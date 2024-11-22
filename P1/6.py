'''Escreva um código que gere uma lista de números aleatórios entre e 50 e, em seguida, imprima quantos números são ímpares.'''

contador_1 = 0
contador_2 = 0


for i in range(1, 51):
    divisao = i % 2 
    
    if divisao == 0:
        contador_1 += 1
    
    else:
        contador_2 += 1
        
print("Qantidade de núemeros ímpares: ", contador_2)
print("Quantidade de núemros pares: ", contador_1)
