def numeros_primos_ate(n):
    if n < 2:
        return []
    primos = []
    for num in range(2, n + 1):
        for divisor in range(2, int(num ** 0.5) + 1):
            if num % divisor == 0:
                break
        else:
            primos.append(num)
    return primos

print(numeros_primos_ate(10))