def soma_digitos(n):
    if n < 10:  # Caso base: se o número tem apenas um dígito, retorna o próprio número
        return n
    return n % 10 + soma_digitos(n // 10)  # Soma o último dígito com o resultado recursivo para o restante

# Exemplo de uso:
num = 678
print(soma_digitos(num))  
