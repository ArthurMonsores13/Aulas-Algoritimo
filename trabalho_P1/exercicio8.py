'''Crie um programa que peça um número e verifique se ele é primo.'''

num = int(input("Digite um número e eu te dizer se ele é primo ou não: "))

if num < 2:
    print("Não é um número primo!")

else:
    primo = True

    for i in range(2,num):
        if num % i == 0:
            primo = False
            break

    if primo == True: 
        print("Número primo!")

    else:
        print("Não é um número primo!")