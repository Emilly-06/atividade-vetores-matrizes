
# Controle de chamados

dias = ["Segunda", "Terca", "Quarta", "Quinta", "Sexta"]
chamados = []

for dia in dias:
    quantidade = int(input("Chamados de " + dia + ": "))

    while quantidade < 0:
        print("Nao pode ser negativo!")
        quantidade = int(input("Digite novamente: "))

    chamados.append(quantidade)

total = sum(chamados)
media = total / 5
maior = max(chamados)

print("\n--- RELATORIO ---")

for i in range(5):
    print(dias[i], ":", chamados[i], "chamados")

print("Total:", total)
print("Media:", media)

print("Dia com mais chamados:")

for i in range(5):
    if chamados[i] == maior:
        print(dias[i])

print("Dias acima da media:")

for i in range(5):
    if chamados[i] > media:
        print(dias[i])

# Consulta de chamados
dia = input("Digite o dia para consultar: ").capitalize()

if dia in dias:
    posicao = dias.index(dia)
    print("Chamados:", chamados[posicao])
else:
    print("Dia nao encontrado.")
