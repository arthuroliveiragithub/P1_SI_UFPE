#Considere um arquivo texto com nome externo ´discipold.txt´,
# contendo informações de disciplinas (Código com 5 posições,
# nome com 35 posições e créditos com 2 posições), uma disciplina
# por linha. Faça um programa Python para criar um segundo arquivo
# com nome externo ´discipnew.txt´ contendo informações das mesmas
# disciplinas, mas com as seguintes modificações:
#
#As disciplinas cujos códigos são IF125 e IF380 devem ser excluídas,
# i.e., não devem ser gravadas no novo arquivo.
#
#Os números de créditos das disciplinas cujos códigos começam por MA
# devem ser alterados para 5.
#
#O novo arquivo terá um campo a mais (carga horária, com 3 posições)
# cujo valor deve ser o número de créditos da disciplina  multiplicado por 15.
#
#No final o seu programa deve imprimir o número de disciplinas de cada
# arquivo e também o número de disciplinas que tiveram seus números de
# créditos alterados.

try:
    leitura = open('discipold.txt', 'r')
    escrita = open('discipnew.txt', 'w')

    tot_discipold = tot_discipnew = tot_discip_alt = 0
    with leitura, escrita:
        for linha in leitura:
            codigo = linha[0:5]
            nome = linha[6:41]
            credito = linha[42:44]

            tot_discipold += 1
            if (codigo != 'IF125') and (codigo != 'IF125'):
                if codigo[0:2] == 'MA':
                    tot_discip_alt += 1
                    credito = '5'

                tot_discipnew += 1
                carga_horaria = int(credito) * 15

                escrita.write(f'{codigo} {nome} {credito:2} {str(carga_horaria):3}\n')

except FileNotFoundError:
    print("Arquivo não encontrado.")
except PermissionError:
    print("Sem permissão.")

