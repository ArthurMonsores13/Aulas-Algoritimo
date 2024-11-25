def subconjuntos(lista):
    if not lista:  # Caso base: lista vazia tem apenas o subconjunto vazio
        return [[]]
    # Remove o primeiro elemento e calcula os subconjuntos do restante
    subconjuntos_sem_primeiro = subconjuntos(lista[1:])
    # Adiciona o primeiro elemento a cada subconjunto já gerado
    subconjuntos_com_primeiro = [[lista[0]] + subconjunto for subconjunto in subconjuntos_sem_primeiro]
    # Combina os subconjuntos com e sem o primeiro elemento
    return subconjuntos_sem_primeiro + subconjuntos_com_primeiro

# Exemplo de uso:
lista = [5,4]
print(subconjuntos(lista))  
# Saída: [[], [2], [1], [1, 2]]
