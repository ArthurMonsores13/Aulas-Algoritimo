def fibonacci(n, memo={}):
    if n in memo:  # Verifica se o resultado já foi calculado
        return memo[n]
    if n <= 1:  # Caso base: Fibonacci(0) = 0, Fibonacci(1) = 1
        return n
    # Calcula o valor e armazena no dicionário
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

# Exemplo de uso:
n = 10
print(fibonacci(n))  
