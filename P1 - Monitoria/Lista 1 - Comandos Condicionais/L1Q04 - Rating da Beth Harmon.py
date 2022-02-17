rating_beth = int(input())
rating_adv = int(input())
resultado_partida = input()
saida = ''

e = 1/(1 + 10**((rating_adv - rating_beth)/400))

if resultado_partida == "vitoria":
    rating_beth = int(rating_beth + 40 * (1 - e))
    saida = rating_beth
elif resultado_partida == "empate":
    rating_beth = int(rating_beth + 40 * (0.5 - e))
    saida = rating_beth
elif resultado_partida == "derrota":
    rating_beth = int(rating_beth + 40 * (0 - e))
    saida = rating_beth
else:
    saida = "Resultado da partida invalido"

print(saida)
