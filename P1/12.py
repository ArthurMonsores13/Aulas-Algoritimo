'''Crie um programa que receba um número inteiro positivo e imprima tabela de muliplicação desse número (de 1 a 10).
'''

num = int(input("Digite um número inteiro e positivio: "))

for i in range(0, 11):
    mult = num * i 
    print(mult) 