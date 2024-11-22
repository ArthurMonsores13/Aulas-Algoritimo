lista = []

while True:
    num = input("Digite um número ou parar para encerrar o loop: ")
    
    if num.lower() == "parar":
        print('Looping encerrado!')
        break
    
    elif num.isnumeric():
        num = int(num)
        lista.append(num)
        
    else:
        print("Digite um valor válido!")
        
print("Sua lista de números é: ", lista)

soma = sum(lista)

print("A soma da sua lista é: ", soma)