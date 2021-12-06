tabela = {}
qtd = 0

cpf = input("Digite o CPF do funcionário: ")
while len(cpf) != 11:
    cpf = input("Digite um CPF válido, com 11 dígitos: ")
cpf = int(cpf)

while (cpf != '0') and (qtd < 150):
    qtd += 1
    nome = input("Digite o nome do funcionário: ")
    genero = input("Digite o gênero do funcionário (M ou F): ")
    while (genero != 'M') and (genero != 'F'):
        genero = input("Digite a sigla correta (M ou F): ")
    numDep = int(input("Digite o número de dependentes: "))
    while numDep < 0:
        numDep = int(input("Valor inválido! Digite o número de dependentes: "))
    tabela[cpf] = (nome, genero, numDep)

    cpf = input("Digite o CPF do próximo funcionário ou 0 para encerrar: ")
    while len(cpf) != 11 and cpf != '0' and cpf != tabela[qtd-1]:
        cpf = input("Digite um CPF válido, com 11 dígitos, ou 0 para encerrar: ")
        if cpf == '0':
            break
    cpf = int(cpf)

if qtd == 150:
    print("Número máximo de funcionários atingido.")

entradaGenero = input("Digite o gênero (M ou F) desejado: ")
while (entradaGenero != 'M') and (entradaGenero != 'F'):
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
    if tabela[cpf][3] >= 2*entradaNumDep:
        qtdDob += 1

print(f"A quantidade de pessoas selecionadas foi: {qtdSel}.\n"
      f"A quantidade de pessoas que têm pelo menos o dobro do número de dependentes foi: {qtdDob}.\n"
      f"A quantidade total de pessoas na tabela foi: {qtd}.")
