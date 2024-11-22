lista_funcionarios = []

while True:
    print(" 1 - Cadastrar , 2 - Excluir , 3 - listar , 4 - encerrar", "\n")
    opcoes = int(input("Escolha entre as seguintes opções: "))
    
    if opcoes > 4:
        print("Escolha um opção válida", "\n")
        
    elif opcoes == 1:
        novo_funcionario = input("Digite o nome completo do funcionário que deseja cadastrar: ")
        lista_funcionarios.append(novo_funcionario)
        print("Cadastro concluído!", "\n")
    elif opcoes == 2:
        excluir_fucionario = input("Digite o nome do funcionário que deseja excluir: ")
        lista_funcionarios.pop(lista_funcionarios.index(excluir_fucionario))
        print("Funcionário excluido com sucesso!", "\n")
    elif opcoes == 3:
        print("A lista de funcionárioa atual é: ", lista_funcionarios)
    elif opcoes == 4:
        print("Programa encerrado!")
        break        