'''Crie um programa que exiba a sequência de Fibonacci até o enésimo termo, onde o usuário fornece o valor de n.'''
'''
n = 100
t1 = 0
t2 = 1
print(" {} -> {} ".format(t1, t2), end="")
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(" -> {} ".format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
'''

n = int( input(" Digite quantos termos você deseja :"))
t1 = 0
t2 = 1
print(" {} -> {} ".format(t1, t2), end="")
cont = 3

while cont <= n:
    t3 = t1 + t2
    print(" -> {} ".format(t3), end="")
    t1 = t2
    t2 = t3
    cont += 1
