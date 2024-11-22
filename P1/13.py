'''Escreva um código que solicite ao usuário uma lista de números e imprima a média, o maior e ○ menor número da lista
'''

lista = []

while True:
    num = int(input("Digite os números para adcionar a lista ou 0 para encerrar: "))
    
    if num== 0:
        break
    
    elif num != 0:
        lista.append(num)
        
        
cont = 0
maior_num = lista[0]
menor_num = lista[0]


for num in lista:
    cont += 1

    if num > maior_num:
        maior_num = num
        
    elif num < menor_num:
        menor_num = num

soma = sum(lista)
media = soma / cont

print("A média dos números digitados é: ",media)
print("O maior númeor da lista é: ",maior_num)
print("O menor número da lista é: ",menor_num)

