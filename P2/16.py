def potencia(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * potencia(x, n - 1)
    else:
        return 1 / potencia(x, -n)

# Exemplo de uso:
print(potencia(2, 3))   # Saída: 8 (2^3)
print(potencia(2, -5))  # Saída: 0.125 (2^-3)
print(potencia(5, 0))   # Saída: 1 (5^0)
