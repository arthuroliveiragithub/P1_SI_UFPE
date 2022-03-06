# https://www.dikastis.com.br/problems/01FW86J15Y6KKGS97N2YDHJWFH

letra_n = input()
qtd_participantes = int(input())
contador = 0
qtd_letras_vencedor = 0
vencedor = ''
palavra_vencedora = ''

while contador < qtd_participantes:
    nome, palavra = input().split('-')
    contador_letras = 0
    for letra in palavra:
        if letra == letra_n:
            contador_letras += 1
    if contador_letras > qtd_letras_vencedor:
        qtd_letras_vencedor = contador_letras
        vencedor = nome
        palavra_vencedora = palavra
    contador += 1

if vencedor == 'Prior':
    output = f"Joga y joga! Mago Prior e o novo lider com a palavra {palavra_vencedora} " \
             f"com {qtd_letras_vencedor} aparicoes da letra {letra_n}."
else:
    output = f"Vish! O Mago Prior pode ir pro paredao, ja que quem ganhou foi {vencedor}, " \
             f"com a palavra {palavra_vencedora} e {qtd_letras_vencedor} aparicoes da letra {letra_n}."

print(output)
