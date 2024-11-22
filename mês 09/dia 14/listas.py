# Exemplo de uso de Lista em Python

#Recerber do usuario 5 nomes e, ao final, exiber os 5 nomes

'''nomesDigitados = []

for o in range(1, 6):
    nome = input("Digite seu nome: ")
    nomesDigitados.append(nome)

print("\nOs nomes informados foram: \n")
for o in nomesDigitados:
    print(o)
'''
nomes = ["Marta", "Maria", "Alfredo"]
nomes.pop(nomes.index("Maria"))

print(nomes)

nomes.sort()