nomes = ["Amanda", "Rafaela", "Mirella", "Lívia", "Bernardo"]

# Cria uma lista com os comprimentos dos nomes
comprimentos = [len(nome) for nome in nomes]

# Encontra os índices dos nomes mais longo e mais curto
indice_mais_longo = comprimentos.index(max(comprimentos))
indice_mais_curto = comprimentos.index(min(comprimentos))

# Imprime os nomes correspondentes
print("Nome mais longo:", nomes[indice_mais_longo])
print("Nome mais curto:", nomes[indice_mais_curto])