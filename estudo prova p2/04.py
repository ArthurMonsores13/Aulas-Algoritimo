'''Crie uma função chamada fatorial que recebe um número inteiro não negativo e retorna o fatorial
desse número. Lembre-se que o fatorial de 0 é 1.'''

def fatorial(n):
    resultado = 1
    for i in range(1, n+1):
        resultado = resultado * 1
    return resultado


def fatorialR(n):
    if n ==0:
        return 1
    return n * fatorialR(n-1)

result = fatorialR(3)
print(result)
result = fatorial(0)
print(result)


    