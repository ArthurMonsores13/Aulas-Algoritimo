def substituir_vogais(s, caractere):
    vogais = 'aeiouAEIOU'
    return ''.join(caractere if c in vogais else c for c in s)


print(substituir_vogais("Ola mundo","0"))