# Lista de caracteres (exemplo)
lista = ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'x', 'y', 'z']

# Inicializando os contadores
vogais = 0
consoantes = 0

# Definindo as vogais
vogais_str = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]

# Iterando sobre cada caractere da lista
for caractere in lista:
    if caractere in vogais_str:
        vogais += 1
    else:
        consoantes += 1

# Imprimindo os resultados
print("Vogais:", vogais)
print("Consoantes:", consoantes)