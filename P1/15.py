ano = int(input("Digite um ano: "))

if ano % 4 == 0: 
    if ano % 100 != 0:
        if ano % 400 == 0:
            print("Ano bissexto.")  
        print("Ano bissexto.")  
    print("Ano bissexto.")    
else:
    print("Não é ano bissexto.")
    