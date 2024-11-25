def contar_palavras(lista):
    frequencia = {}
    for palavra in lista:
        palavra = palavra.lower()
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    return frequencia

# Exemplo de uso:
palavras = ["Andar", "andar", "tentar", "Tentar", "comer", "andar"]
print(contar_palavras(palavras))
# Saída: {'palavra': 3, 'texto': 2, 'exemplo': 1}
