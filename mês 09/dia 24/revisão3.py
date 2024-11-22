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

#exemplo while

# receba do usuario n numeros inteiros, até que o usuario informe o valor 0.
# quando isso ocorrer, o programa devera mostrar os somatorios dos valores. 

# while teste logico: 
#    comandos...

soma = 0 
valor = int(input("Digite um valor (0 para sair): "))
soma = soma + valor

while valor != 0:
    valor = int(input("Digite um valor (0 para sair): "))
    soma = soma + valor
print("A soma dos valores digitados é: ", soma)


# outra forma de fazer 

soma = 0

while True:
    valor = int(input("Digite um valor (0 para sair): "))
    soma = soma + valor
    if valor == 0:
        break

print("A soma dos valores digitados é: ", soma)

