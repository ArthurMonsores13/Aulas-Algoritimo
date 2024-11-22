disciplina = ["Algoritmos", "Disciplina chata 1", "Disciplina chata 2"]
#                 0                 1                    2
print(disciplina[0])

print(len(disciplina)) 
#conta quantas elementos tem na lista

for i in disciplina:
    print(i)
#printa todos 

notas = [["Algotimos", 10], ["Laborotorio de Web Sites", 4], ["Analise de requisitos", 7]]
#                 0                    1                               2
#              0        1                     0          1          0                  1
# uma lista dentro de uma lista
print(notas[0])

times = ["flamengo", 0 , True, "america", 10, False]
# poder do python, adcionar varios tipos em uma unica lista

print(times[0:2])
#mostra tudo ate o 2 (o 2 não entra)

print(times[:3])
#0 ate o 3
print(times[3:])
#do 3 ate o final

#Como mostrar elementos alternados na lista???

for i in range(0, len(times)):
    if i == 1 or i ==2 or i ==4 or i ==5:
        print(times[i])
        
        
print(times[1::2])

nome = ["VIirginlado"]

print(dir(nome))
#mostra as funçõpes 

print(dir(disciplina))

disciplina.append("Engenharia de requisitos")
# add ao final

print(disciplina)

nomes = []
# lista em branco 

nomes.append("Amanda")

print(nome)

nomes =[]

nome = input("Qual seu nome? ")

nomes.append(nome)  
print(nomes)

