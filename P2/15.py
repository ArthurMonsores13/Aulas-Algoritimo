def eh_palindromo(num):
    num_str = str(num)
    return num_str == num_str[::-1]

# Exemplo de uso:
print(eh_palindromo(121))  # Saída: True
print(eh_palindromo(232))  # Saída: False
