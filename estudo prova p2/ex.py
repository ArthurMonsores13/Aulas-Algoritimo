def calc_area(base = 10, altura = 50):
    #calculo de area
    return base*altura

def range(limif, limsup, passo=1):
    range(1,10)
    
#programa principal
print("Calculo da area")
b1 = int(input("Informe o valor da base: "))
h1 = int(input("Informe o valor da altura: "))

area = calc_area(b1, h1)
print("A area calculada foi: ", area)

#o que está fora da função não enxerga oq esta dentro da função e vise versa

print("Area teste: ", calc_area(5))


def montamenu():
    #função para apresentar um menu de opções padão para um CRUD
    print("Menu principal")
    print("1 - Cadastrar")
    print("2 - Consultar")
    print("3 - Alterar")
    print("4 - Excluir")
    print("5 - Sair")
    opt1 = int(input("Digite a opção desejada: "))
    return(opt1)

while True:
#programa principal
    opcao = montamenu()
    if opcao == 5:
        break
    else:
        print("A opção escolhida foi: ", opcao)
        print("Rotina ainda não implementada...")

print("Programa finalizado!")