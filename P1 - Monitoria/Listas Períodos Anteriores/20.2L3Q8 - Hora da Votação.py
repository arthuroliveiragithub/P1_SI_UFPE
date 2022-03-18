votantes = []
votados = []
nao_votou, votos, max_votos = 0, 0, 0
expulso = ''
output = ''
empate = False
impostor_votou = False

n_votos = int(input())
impostor = input()
for i in range(n_votos):
    votante, votado = input().split(": ")
    votantes.append(votante)
    votados.append(votado)

for participante in votados:
    votou = False
    for nome in votantes:
        if nome == participante:
            votou = True
    if not votou:
        nao_votou += 1

for nome in votantes:
    if nome == impostor:
        impostor_votou = True
if not impostor_votou:
    nao_votou += 1

for nome in votantes:
    empate = False
    votos = votados.count(nome)
    if votos > max_votos:
        max_votos = votos
        expulso = nome
    elif votos == max_votos:
        empate = True

if nao_votou > 0:
    output = f"Votação incompleta. Faltam votos de {nao_votou} jogadores"
else:
    if not empate:
        if expulso == impostor:
            output = f"{expulso} foi expulso com {max_votos} votos. Ele era o IMPOSTOR"
        elif expulso != impostor:
            output = f"{expulso} foi expulso com {max_votos} votos. Ele era INOCENTE"
    else:
        output = "Empate. Ninguem foi expulso"

print(output)
