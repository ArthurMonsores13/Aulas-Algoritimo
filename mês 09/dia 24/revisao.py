'''
operadores lógicos = so pode retornar true ou false

and = e
or = ou 
not = não

'''

print("Cáculo de desconto do IRRF")
salario = float(input('Informe seu salário: '))

if salario < 3000:
    desconto = 0
elif salario >= 3000 and salario < 5000:
    desconto = salario * 5 / 100
elif salario >= 5000 and salario < 7000:
    desconto = salario * 10 / 100
elif salario >= 7000 and salario <9000:
    desconto = salario * 15 / 100
else:
    desconto = salario * 27.5 / 100



    print("Salario com IRRF")
    print("seu salario bruto é: ", salario)
    print("Desconto...........:", desconto)
    print("Salario liquido....:", salario - desconto)