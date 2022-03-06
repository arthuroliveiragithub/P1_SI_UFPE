# https://www.dikastis.com.br/problems/01FW71V72KKG76CNYJW76MEN69

n = int(input())
jogador1 = input()
jogador2 = input()
jogador3 = input()
pontuacao1 = pontuacao2 = pontuacao3 = 0
contador = 0

# primeira etapa:
while contador < n and (pontuacao1 < 200 and pontuacao2 < 200 and pontuacao3 < 200):
    for i in range(3):
        jogada = int(input())
        if i == 0:
            pontuacao1 += jogada
        elif i == 1:
            pontuacao2 += jogada
        elif i == 2:
            pontuacao3 += jogada
    contador += 1

# comparando resultados da primeira etapa:
if pontuacao1 < pontuacao2:
    pontuacao2, pontuacao1 = pontuacao1, pontuacao2
    jogador2, jogador1 = jogador1, jogador2
if pontuacao2 < pontuacao3:
    pontuacao3, pontuacao2 = pontuacao2, pontuacao3
    jogador3, jogador2 = jogador2, jogador3
if pontuacao1 < pontuacao2:
    pontuacao2, pontuacao1 = pontuacao1, pontuacao2
    jogador2, jogador1 = jogador1, jogador2

# imprimindo resultados da primeira etapa:
print(f"{jogador3} ja esta confirmado no paredao")
print(f"1° - {jogador1}")
print(f"2° - {jogador2}")

# segunda rodada - final:
pontuacao1 = pontuacao2 = 0
contador = 0
n = int(input())
while contador < n:
    for i in range(2):
        jogada = int(input())
        if i == 0:
            pontuacao1 += jogada
        elif i == 1:
            pontuacao2 += jogada
    contador += 1

# comparando resultados da segunda rodada - final:
if pontuacao1 > pontuacao2:
    frase = f"Nosso paredao sera entre {jogador2} e {jogador3}"
else:
    frase = f"Nosso paredao sera entre {jogador1} e {jogador3}"
print(frase)
