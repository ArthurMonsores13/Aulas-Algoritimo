def substirur_vogais(texto, vogal):
    vogais = "aeiouAEIOU"
    texto_novo = ""
    
    for letra in texto:
        if letra in vogais:
            texto_novo += vogal
        else:
            texto_novo += letra
    return texto_novo
            
print(substirur_vogais("Amanda", "e"))


