'''Crie um programa que solicite ao usuário uma lista de números e imprima a lista em ordem crescente, sem utilizar a função sort()'''

crescente = []

while True:
    lista = int(input("Digite números para colocar na sua lista ou 0 para sair: "))

    if lista == 0:
        break

    i = 0
    while i < len(crescente) and lista > crescente[i]:
        i += 1

    crescente.insert(i, lista)

print(crescente)