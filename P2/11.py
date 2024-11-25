def combinacoes(lista, r):
    if r == 0:
        return [[]]
    if not lista:
        return []
    with_first = [[lista[0]] + c for c in combinacoes(lista[1:], r - 1)]
    without_first = combinacoes(lista[1:], r)
    return with_first + without_first

# Exemplo de uso:
lista = [1, 2, 3, 4]
r = 3
print(combinacoes(lista, r))
