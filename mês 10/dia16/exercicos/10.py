def conta_palavras(texto):

    palavras = texto.split()

    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem 

texto = "Amanda da Silva Diniz Nogueira"
print(conta_palavras(texto))