# Q2 – Faça um programa Python para ler um arquivo chamado “comprasClientes.txt” contendo
# código da compra (int, 5 colunas), código do cliente (int, 4 colunas), e as quantidades (int, 2
# colunas) + valores unitários (float, 6 colunas, 2 decimais) em Reais de até 4 itens comprados
# de vários clientes em uma loja, uma compra/cliente por linha, com os dados separados por um
# espaço em branco. Observe que compras com menos de 4 itens terão zeros nas quantidades e
# valores unitários dos outros itens.
# OBS: Um pequeno arquivo de teste será fornecido juntamente com a questão.
# O programa deve gravar um segundo arquivo com o código da compra e do cliente bem
# como o valor total de cada compra (float, 9 colunas, 2 decimais), uma compra por linha. Ou
# seja, o arquivo gravado terá a mesma quantidade de linhas do arquivo lido.
# O cálculo do valor total de cada compra deve ser feito em uma subrotina do tipo função,
# chamada calculaTotal, que deve receber como parâmetro um string único, com o pedaço da
# linha do arquivo que contém as quantidades e valores unitários dos (até) 4 itens da compra, e
# deve devolver como resultado o valor total da compra em Reais.
# No início da execução do programa, o usuário informará o nome e o formato do arquivo
# a ser gravado: 1=texto-simples ou 2=texto-csv. No formato 1 o nome externo do arquivo deve
# terminar com “.txt” e as informações de cada compra são separadas por espaço em branco,
# enquanto que no formato 2 o nome externo do arquivo deve terminar com “.csv’” e as
# informações de cada compra são separadas por ";" (ponto-e-vírgula).
# No final o programa deve imprimir a quantidade de registros gravados no arquivo bem
# como o faturamento total da loja referente às compras gravadas no mesmo.


def calculaTotal(string):
    lista = string.split()
    totalCompra = (int(lista[0]) * float(lista[1]) +
                   int(lista[2]) * float(lista[3]) +
                   int(lista[4]) * float(lista[5]) +
                   int(lista[6]) * float(lista[7]))
    return totalCompra

try:
    arquivo = input("Digite o nome do arquivo de saída: ")
    formato = int(input("Digite o código do formato desejado (1-texto simples 2-texto-csv): "))
    while formato != 1 and formato != 2:
        formato = int(input("Digite o código do formato desejado (1-texto simples 2-texto-csv): "))
    qtdRegistros = total = 0

    if formato == 1:
        escrita = open(f'{arquivo}.txt', 'w')
    else:
        escrita = open(f'{arquivo}.csv', 'w')

    leitura = open('comprasClientes.txt', 'r')
    with leitura, escrita:
        for linha in leitura:
            codCompra = linha[0:5]
            codCliente = linha[6:10]
            string = linha[11:50]
            if formato == 1:
                escrita.write(f'{codCompra} {codCliente} {calculaTotal(string):.2f}\n')
            else:
                escrita.write(f'{codCompra};{codCliente};{calculaTotal(string):.2f}\n')
            total += calculaTotal(string)
            qtdRegistros += 1
except FileNotFoundError:
        print("Arquivo não encontrado.")
except PermissionError:
        print("Sem permissão de escrita.")
else:
    print(f'Quantidade de registros: {qtdRegistros}\n'
          f'Faturamento total da loja: R$ {total:.2f}')
