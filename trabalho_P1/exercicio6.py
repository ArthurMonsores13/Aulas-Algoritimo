'''Crie um programa que calcule o fatorial de um número fornecido pelo usuário.'''

num = int(input("Digite um número e eu vou calcular o fatorial desse número: "))

resultado = 1

for i  in range(1,num + 1):
    resultado *= i 

print(resultado)

