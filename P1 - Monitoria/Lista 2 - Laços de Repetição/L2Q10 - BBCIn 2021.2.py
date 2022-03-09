# https://www.dikastis.com.br/problems/01FWBY882HFGMFADJ7PXQVKTJH

vida1 = vida2 = 100
dano1 = dano2 = 0
rodada = 1
fraseLucas = "Foi uma prova dificil, mas Lucas mostra como se faz e vence o BBCIn do 2021.2!!"
fraseSeverino = "Foi uma prova dificil, mas Severino mostra como se faz e vence o BBCIn do 2021.2!!"
fraseEmpate = "Pela primeira vez na historia, ha um empate e ambos irao " \
                        "levar para casa o grande premio do BBCIn do 2021.2!!"
fim = False

while not fim:
    acao1 = input()
    acao2 = input()

    if rodada == 4:
        vida1, vida2 = vida2, vida1
    elif rodada == 7:
        vida1 -= (dano2 + 0.5 * dano2 + 0.25 * dano2)
        vida2 -= (dano1 + 0.5 * dano1 + 0.25 * dano1)
    elif rodada == 10:
        if vida1 > vida2:
            vida2 = vida1
        elif vida2 > vida1:
            vida1 = vida2
    else:
        if acao1 == "Golpe Rapido":
            if acao2 == "Golpe Rapido":
                dano1 = dano2 = 12
                vida1 -= dano2
                vida2 -= dano1
            elif acao2 == "Golpe Forte":
                dano2 = 25
                vida1 -= dano2
            elif acao2 == "Bloqueio":
                dano1 = 0.5 * 12
                vida2 -= dano1
            elif acao2 == "Esquivar":
                dano1 = 12
                vida2 -= dano1
        elif acao1 == "Golpe Forte":
            if acao2 == "Golpe Rapido":
                dano1 = 25
                vida2 -= dano1
            elif acao2 == "Golpe Forte":
                dano1 = dano2 = 0
            elif acao2 == "Bloqueio":
                dano1 = 20
                vida2 -= dano1
            elif acao2 == "Esquivar":
                dano2 = 20
                vida1 -= dano2
        elif acao1 == "Bloqueio":
            if acao2 == "Golpe Rapido":
                dano2 = 0.5 * 12
                vida1 -= dano2
            elif acao2 == "Golpe Forte":
                dano2 = 20
                vida1 -= dano2
        elif acao1 == "Esquivar":
            if acao2 == "Golpe Rapido":
                dano2 = 12
                vida1 -= dano2
            elif acao2 == "Golpe Forte":
                dano1 = 20
                vida2 -= dano1
        else:
            dano1 = dano2 = 0

    if vida1 > 0 and vida2 > 0:
        if rodada < 12:
            rodada += 1
        else:
            fim = True
            if vida1 > vida2:
                print(fraseLucas)
            elif vida1 < vida2:
                print(fraseSeverino)
            elif vida1 == vida2:
                print(fraseEmpate)
    else:
        fim = True
        if vida1 <= 0:
            print(fraseSeverino)
        elif vida2 <= 0:
            fim = True
            print(fraseLucas)
