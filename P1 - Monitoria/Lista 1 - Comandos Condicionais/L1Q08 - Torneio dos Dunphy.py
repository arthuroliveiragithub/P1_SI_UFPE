# https://www.dikastis.com.br/problems/01FV5M82WTEHVQZS8D93FRRJPG

nome_1 = input()
pontuacao_1 = int(input())
nome_2 = input()
pontuacao_2 = int(input())
nome_3 = input()
pontuacao_3 = int(input())

if pontuacao_1 > pontuacao_2 or (pontuacao_1 == pontuacao_2 and nome_1 > nome_2):
    pontuacao_1, pontuacao_2 = pontuacao_2, pontuacao_1
    nome_1, nome_2 = nome_2, nome_1
if pontuacao_2 > pontuacao_3 or (pontuacao_2 == pontuacao_3 and nome_2 > nome_3):
    pontuacao_2, pontuacao_3 = pontuacao_3, pontuacao_2
    nome_2, nome_3 = nome_3, nome_2
if pontuacao_1 > pontuacao_2 or (pontuacao_1 == pontuacao_2 and nome_1 > nome_2):
    pontuacao_1, pontuacao_2 = pontuacao_2, pontuacao_1
    nome_1, nome_2 = nome_2, nome_1

print(f"{nome_1} {pontuacao_1}\n"
      f"{nome_2} {pontuacao_2}\n"
      f"{nome_3} {pontuacao_3}")
