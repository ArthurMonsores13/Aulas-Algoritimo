def torre_de_hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mova o disco 1 da estaca {origem} para a estaca {destino}")
        return
    torre_de_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} da estaca {origem} para a estaca {destino}")
    torre_de_hanoi(n - 1, auxiliar, destino, origem)

# Exemplo de uso:
n = 2
torre_de_hanoi(n, 'A', 'C', 'B')
