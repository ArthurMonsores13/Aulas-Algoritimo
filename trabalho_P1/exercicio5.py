'''Crie um programa que peça números até que o usuário digite um número negativo. Exiba a quantidade de números positivos digitados.'''

contador = 0 

while True:
    valor = float(input("Digite um valor positivo ou um negativo para acabar o loop: "))

    if valor < 0:
        break

    contador  += 1
    
print("A quantidade de valor positivos digitados foi: ", contador) 