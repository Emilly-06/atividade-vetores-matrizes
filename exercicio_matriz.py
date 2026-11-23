
# Controle de vendas da feira

produtos = ["Camisetas", "Canecas", "Bones"]

periodos = ["Qui manha", "Qui tarde", "Sex manha", "Sex tarde"]

matriz = []

# Preenchendo a matriz
for produto in produtos:
    linha = []

    print("\n", produto)

    for periodo in periodos:
        quantidade = int(input("Vendas em " + periodo + ": "))

        while quantidade < 0:
            print("Nao pode ser negativo!")
            quantidade = int(input("Digite novamente: "))

        linha.append(quantidade)

    matriz.append(linha)

print("\n--- RELATORIO DE VENDAS ---")

total_geral = 0
totais_produtos = []

# Total de cada produto
for i in range(3):
    total = sum(matriz[i])
    totais_produtos.append(total)
    total_geral += total

    print(produtos[i], ":", total, "vendas")

# Total de cada periodo
print("\nTotal por periodo:")

for j in range(4):
    total = 0

    for i in range(3):
        total += matriz[i][j]

    print(periodos[j], ":", total)

print("\nTotal geral:", total_geral)

# Produto mais vendido
maior = max(totais_produtos)

print("\nProduto mais vendido:")

for i in range(3):
    if totais_produtos[i] == maior:
        print(produtos[i])

# Periodo com mais vendas
totais_periodos = []

for j in range(4):
    total = 0

    for i in range(3):
        total += matriz[i][j]

    totais_periodos.append(total)

maior_periodo = max(totais_periodos)

print("\nPeriodo com mais vendas:")

for j in range(4):
    if totais_periodos[j] == maior_periodo:
        print(periodos[j])
