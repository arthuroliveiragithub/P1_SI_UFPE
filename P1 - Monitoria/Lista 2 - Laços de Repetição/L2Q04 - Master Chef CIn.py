# https://www.dikastis.com.br/problems/01FW9P5NEFCAEZR52ND3G4ZK47

eliminado = ''
media_eliminado = 10
contador_chefes = 1
n_chefes = int(input())

while contador_chefes <= n_chefes:
    nome_chefe = input()
    contador_notas = 0
    media_notas = 0
    for contador_notas in range(3):
        nota = float(input())
        while nota > 10:
            nota = float(input())
        media_notas += nota
    media_notas = media_notas / (contador_notas + 1)
    if media_notas <= media_eliminado:
        media_eliminado = media_notas
        eliminado = nome_chefe
    contador_chefes += 1

if media_eliminado > 0:
    output = f"O chef eliminado da vez é: {eliminado} - {media_eliminado:.2f}"
else:
    output = f"Ocorreu um erro no sistema de notas, por favor insira notas validas"

print(output)
