tabela = {}
qtd = 0

cpf = int(input("Digite o CPF do funcionário: "))
while len(cpf) != 11 and cpf != 0:
    cpf = int(input("Digite um CPF válido, com 11 dígitos: "))

while (cpf != 0) and (qtd < 150):
    qtd += 1
    nome = input("Digite o nome do funcionário: ")
    genero = input("Digite o gênero do funcionário (M ou F): ")
    while (genero != "M") or (genero != "F"):
        genero = input("Digite a sigla correta (M ou F):")
    numDep = int(input("Digite o número de dependentes: "))
    while numDep < 0:
        numDep = int(input("Valor inválido! Digite o número de dependentes: "))
    tabela[cpf] = (nome, genero, numDep)

    cpf = int(input("Digite o CPF do próximo funcionário ou 0 para encerrar: ")
    while (cpf != 0) and (len(cpf) != 11):
        cpf = int(input("Digite um CPF válido, com 11 dígitos, ou 0 para encerrar: "))

if qtd == 150:
    print("Número máximo de funcionários atingido.")

entradaGenero = input("Digite o gênero (M ou F) desejado: ")
while (entradaGenero != "M") or (genero != "F"):
    genero = input("Digite a sigla correta (M ou F):")
entradaNumDep = int(input("Digite o número de dependentes desejado: "))
while entradaNumDep < 0:
    numDep = int(input("Valor inválido! Digite o número de dependentes: "))

qtdSel = 0
qtdDob = 0
for cpf in tabela:
    if tabela[cpf][2] == entradaGenero and tabela[cpf][3] >= entradaNumDep:
        qtdSel += 1
        print(tabela[cpf][1], tabela[cpf][3])
    if (tabela[cpf][3] >= 2*entradaNumDep):
        qtdDob += 1

print(f"A quantidade de pessoas selecionadas foi: {qtdSel}.\n"
      f"A quantidade de pessoas que têm pelo menos o dobro do número de dependentes foi: {qtdDob}.\n"
      f"A quantidade total de pessoas na tabela foi: {qtd}.")
