def elementos_duplicados(lista):
    contagem = {}
    for elemento in lista:
        contagem[elemento] = contagem.get(elemento, 0) + 1
    return [elemento for elemento, qtd in contagem.items() if qtd > 1]

# Exemplo de uso:
lista = [1, 2, 3, 4, 2, 5]
print(elementos_duplicados(lista))  # Saída: [2, 3]
