# https://www.dikastis.com.br/problems/01FVJRJXER785NF56KS6AGT618

n_chances = 3
letras_anteriores = ''
l1 = l2 = l3 = l4 = l5 = l6 = l7 = l8 = l9 = l10 = l11 = l12 = '-'
frase = ''
frase_completa = "PROVA-DO-ANJO-BBB"
output = ''

while n_chances > 0 and frase != frase_completa:
    letra = input().upper()
    letra_repedida = False
    acertou = False
    for i in range(0, len(letras_anteriores)):
        if letras_anteriores[i] == letra:
            letra_repedida = True
            print(f"Voce ja digitou a letra {letra}")
            print(frase)
    if letra_repedida is False:
        letras_anteriores += letra
        for j in range(0, len(frase_completa)):
            if frase_completa[j] == letra:
                acertou = True
                if j == 0:
                    l1 = letra
                elif j == 1:
                    l2 = letra
                elif j == 2:
                    l3 = l7 = l11 = letra
                elif j == 3:
                    l4 = letra
                elif j == 4:
                    l5 = l8 = letra
                elif j == 6:
                    l6 = letra
                elif j == 10:
                    l9 = letra
                elif j == 11:
                    l10 = letra
                elif j == 14:
                    l12 = letra
        frase = str(l1 + l2 + l3 + l4 + l5 + '-' + l6 + l7 + '-' + l8 + l9 + l10 + l11 + '-' + l12 * 3)
        if acertou:
            print(f"Parabens, voce conseguiu mais uma letra!")
            print(frase)
        else:
            n_chances -= 1
            if n_chances > 0:
                print(f"Que pena, voce tem mais {n_chances} chances!")
                print(frase)
else:
    if n_chances == 0:
        output = "Fim de jogo, sem almoco do anjo pra voce!"
    if frase == frase_completa:
        output = "Boa, voce e o novo Anjo da semana!"
    print(output)
