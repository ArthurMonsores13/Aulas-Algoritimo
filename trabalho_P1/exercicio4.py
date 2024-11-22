'''Crie um programa que peça 5 notas ao usuário e calcule a média.'''

cont = 0 

while True:
    nota = float(input("Digite sua nota: "))

    cont += 1 

    if cont > 4:
        break

media = (nota) / 5

print("A sua média é: ", media)