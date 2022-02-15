#Considere um arquivo texto com nome externo 'discip.txt', contendo
# informações de disciplinas: código com 5 posições, nome com 35 posições,
# créditos com 2 posições, e código do centro a que pertence com 3 posições;
# uma disciplina por linha.

#Considere também um outro arquivo texto nome externo 'centros.txt',
# contendo informações de centros: código com 3 posições e nome com
# 5 posições; também um centro por linha.

#Faça um programa Python para:
#- Usando um procedimento, ler o arquivo de centros e colocar seu conteúdo
# em uma tabela.
#- Gravar um arquivo texto com nome externo 'discipCompleto.txt', contendo
# todas as informações do arquivo 'discip.txt' e mais o nome do centro a
# que pertence.
#- Escrever uma função para achar o nome do centro a partir do seu código.
#- No final imprimir a quantidade de disciplinas e de centros.


def leitura_centro(dict): #procedimento é uma função que não tem retorno
    with open('centros.txt', 'r') as leitura:
        for linha in leitura:
            codigo = linha[0:3]
            centro = linha[4:29]
            dict[codigo] = centro


#def retorna_centro(dict, codigo_centro):
#   return dict[codigo_centro]

try:
    dict = {}
    leitura_centro(dict)
    leitura = open('discip.txt', 'r')
    escrita = open('discipCompleto.txt', 'w')

    tot_discip = 0
    tot_centro = len(dict)
    with leitura, escrita:
        for linha in leitura:
            tot_discip += 1
            codigo = linha[0:5]
            nome = linha[6:41]
            credito = linha[42:44]
            codigo_centro = linha[45:48]
            escrita.write(f'{codigo} {nome} {credito} {codigo_centro} {dict[codigo_centro]}\n')
except FileNotFoundError as msg:
    print(msg)
except PermissionError:
    print("Sem permissão de escrita.")
else:
    print(f'Total de centros: {tot_centro}')
    print(f'Total de disciplinas: {tot_discip}')
# caso não use o comando with, podemos usar o finally para fechar os arquivos
# finally:
#   leitura.close()
#   escrita.close()
