def conta_palavras(s):
    palavras = s.split()
    contagem = {}
    for palavra in palavras:
        palavra = palavra.lower()  
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

texto = "Olá mundo esse e um teste do mundo"
resultado = conta_palavras(texto)
print(resultado)