frase = input("Digite uma frase: ").lower().replace(" ", "")
contador_letras = {}

for letra in frase:
    if letra in contador_letras:
        contador_letras[letra] += 1
    else:
        contador_letras[letra] = 1

print(contador_letras)