def juntar_listas(lista1, lista2):
    return list(set(lista1 + lista2))


print(juntar_listas(["a","b"], ["c","d"]))