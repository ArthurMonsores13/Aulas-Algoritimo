# estrutura de repetição

'''
3 tipos basicos de loop

1 - O numero de repetições é conhecido(para)
    - Nesse caso, vamos utilizar o comando for

2- A repetição deve ocorrer pelo menos uma vez, mas continuar inderterminadamente 
    - executa pelo menos uma vez e fica testando depois...(repita)
    - Nesse caso, vamos utilizar o comando while

3- A repetição deve ocorrer indeterminadamente, mas precisa ser verificada antes de iniciar
    - antes de executar, testa a condição... depois fica testando (repita enquanto)
    - Nesse caso, vamos utilizar o comando while

(inderterminadamente = até enquanto for true ele executa, quando tornar false ele para de executar)
    
'''

# o loop for
'''
loop for na linguagem C
    for (i = 1; i <= 100; i++)
        printf("%d", i);
'''
# !!em python!!
#eu posso colocar o 1 e o 11 em uma varivel e colocar no range tbm
for i in range(1, 101):
    print(i)

time = "framengu"

for i in time:
    print(i)

#listas
times = ["framengu", "fluminense", "america"]

for i in times:
    print(i)

for i in times[0]:
    print(i)


#exibir todos os valores pares 1 e 100
#na prova usar so se for python
for i in range(1, 101):
    if i % 2 == 0: # se o resto for 0 o numero é par
        print(i)

for 1 in range(0, 101, 2): # terceiro parametro é o incremento, o intervalo que mostra os numeros
    print(i)

for i in range(10,0,-1):
    print(i)