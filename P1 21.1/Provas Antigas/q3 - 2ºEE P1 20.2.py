# Q3 – Considere um arquivo texto, cujo nome externo deve ser informado pelo usuário no início,
# contendo as informações dos materiais/estoque da empresa: código (inteiro com 3 posições),
# nome (string com 20 posições), qtdMinima e qtdAtual (ambos inteiros com 4 posições).
# Assuma que tem um espaço em branco separando as informações e que tem um material em
# cada linha do arquivo. Faça um programa Python para ler este arquivo e gravar o arquivo
# texto ‘compras.txt’, contendo informações das compras, também um material por linha:
# código, nome, e qtdCompra (inteiro com 4 posições), que precisam ser feitas para repor o
# estoque, apenas dos materiais que estejam com estoque abaixo do mínimo.
# Você deve escrever e usar uma função calculaCompra que deve receber como parâmetros o
# estoque mínimo e o estoque atual, e retornar como resultado a quantidade a ser comprada. A
# quantidade a ser comprada deve satisfazer a:
# (a) Os materiais que estejam com menos da metade do estoque mínimo devem fazer compras
# para ficar com estoque 20% acima do estoque mínimo.
# (b) Os materiais que estejam com estoque entre 50% e 90% (inclusive) do estoque mínimo
# devem fazer compras para ficar com estoque 10% acima do mínimo.
# (c) Os materiais que estejam com estoque de mais de 90% do estoque mínimo devem fazer
# compras apenas para repor este estoque mínimo.
# OBS - Eventuais valores decimais resultantes das operações envolvendo percentuais devem
# ser truncados (desprezados).


def calculaCompra(qtdMinima, qtdAtual):
    if qtdAtual < 0.5*qtdMinima:
        qtdCompra = qtdMinima - qtdAtual + int(qtdMinima*0.2)
    elif qtdAtual > 0.9*qtdMinima:
        qtdCompra = qtdMinima - qtdAtual
    elif qtdAtual >= 0.5*qtdMinima and qtdAtual <= 0.9*qtdMinima:
        qtdCompra = qtdMinima - qtdAtual + int(qtdMinima * 0.1)
    else:
        qtdCompra = 0
    return qtdCompra


try:
    arquivo = input("Digite o nome do arquivo que contém as informações de estoque: ")
    leitura = open(f'{arquivo}.txt', 'r')
    escrita = open('compras.txt', 'w')
    with leitura, escrita:
        for linha in leitura:
            codigo = linha[0:3]
            nome = linha[4:24]
            qtdMinima = int(linha[25:29])
            qtdAtual = int(linha[30:34])
            qtdCompra = calculaCompra(qtdMinima, qtdAtual)
            if qtdCompra > 0:
                escrita.write(f'{codigo} {nome} {qtdCompra}\n')
except FileNotFoundError as msg:
    print(msg)
except PermissionError:
    print("Sem permissão de escrita.")
else:
    print(f'O arquivo compras.txt contém as informações de compra.')
