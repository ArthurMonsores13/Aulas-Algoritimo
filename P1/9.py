palavras = input("Digite as palavras separadas por espaço: ").split()

contador = 0
for letra in palavras:
    if len(letra) > 5:
        contador += 1

print("Existem", contador, "palavras com mais de 5 letras.")