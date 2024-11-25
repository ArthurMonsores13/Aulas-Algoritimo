def eh_palindromo(s):
    return s == s[::-1]

def conta_palindromos(lista):
    return sum(1 for s in lista if eh_palindromo(s))

# Exemplo de uso:
lista = ["ovo","civic","laranja","onibus"]
print(conta_palindromos(lista))  # Saída: 4 (ana, civic, radar, level)
