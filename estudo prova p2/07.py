def fibonacci(n):
    if n <= 0:
        return []
    sequencia = [0, 1]
    while len(sequencia) < n:
        sequencia.append(sequencia[-1] + sequencia[-2])
    return sequencia[:n]

print(fibonacci(10))