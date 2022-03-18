libero, levantador, central, ponteiro, oposto = 0, 0, 0, 0, 0
time = []
comando, jogador, posicao, nome = '', '', '', ''
fim = False
valido = True

while not fim:
    comando = input()

    if comando == "adicionar":
        jogador = input().split(": ")
        posicao = jogador[1]
        time.append(jogador)

        if posicao == "Libero":
            libero += 1
        elif posicao == "Levantador":
            levantador += 1
        elif posicao == "Central":
            central += 1
        elif posicao == "Ponteiro":
            ponteiro += 1
        elif posicao == "Oposto":
            oposto += 1

        if levantador == 5 or ponteiro == 5 or central == 5 or oposto == 5:
            if posicao == "Levantador":
                saidaErroPosicao = f"Cuidado! voce ja possui 5 levantadores"
            elif posicao == "Central":
                saidaErroPosicao = f"Cuidado! voce ja possui 5 centrais"
            else:
                saidaErroPosicao = f"Cuidado! voce ja possui 5 {posicao.lower()}s"
            print(saidaErroPosicao)
        if libero > 2:
            saidaErroLibero = "ERRO: liberos demais, nao temos uniformes suficientes"
            print(saidaErroLibero)
            fim = True
            valido = False
        if len(time) > 18:
            saidaErroTime = "ERRO: voce estrapolou o numero de jogadores"
            print(saidaErroTime)
            fim = True
            valido = False

    elif comando == "relatorio":
        saidaRelatorio = f"No nosso time ja possuimos:\n" \
                         f"Liberos: {libero}\n" \
                         f"Levantadores: {levantador}\n" \
                         f"Ponteiros: {ponteiro}\n" \
                         f"Centrais: {central}\n" \
                         f"Opostos: {oposto}\n" \
                         f"TOTAL: {len(time)}"
        print(saidaRelatorio)

    elif comando == "nomes":
        posicao = input()
        temPosicao = False
        if posicao == "Libero":
            if libero > 0:
                temPosicao = True
        elif posicao == "Levantador":
            if levantador > 0:
                temPosicao = True
        elif posicao == "Central":
            if central > 0:
                temPosicao = True
        elif posicao == "Ponteiro":
            if ponteiro > 0:
                temPosicao = True
        elif posicao == "Oposto":
            if oposto > 0:
                temPosicao = True

        if temPosicao:
            if posicao == "Levantador":
                saidaTemNomes = f"Os levantadores sao:"
            elif posicao == "Central":
                saidaTemNomes = "Os centrais sao:"
            else:
                saidaTemNomes = f"Os {posicao.lower()}s sao:"
            print(saidaTemNomes)
            for i in range(len(time)):
                if time[i][1] == posicao:
                    print(time[i][0])
        if not temPosicao:
            saidaNaoTemNomes = "Ainda nao temos jogadores nessa posicao"
            print(saidaNaoTemNomes)

    elif comando == "buscar":
        nome = input()
        temNome = False
        for i in range(len(time)):
            if nome == time[i][0]:
                temNome = True

        if temNome:
            if nome == "Samuel":
                saidaTemSamuel = "Sim, Samuel, voce ja esta na lista de jogadores"
                print(saidaTemSamuel)
            else:
                saidaTemJogador = f"Sim, {nome} esta na lista de jogadores"
                print(saidaTemJogador)
        else:
            if nome == "Samuel":
                saidaNaoTemSamuel = "Como voce pode esquecer de si mesmo? Voce nao esta na lista"
                print(saidaNaoTemSamuel)
            else:
                saidaNaoTemJogador = f"O jogador {nome} nao esta na lista de jogadores"
                print(saidaNaoTemJogador)

    elif comando == "fim":
        fim = True

    else:
        saidaInvalido = "***COMANDO INVALIDO***"
        print(saidaInvalido)

if libero != 2:
    valido = False
elif levantador < 2 and central < 2 and ponteiro < 2 and oposto < 2:
    valido = False

if valido:
    eValido = f"O Navegantes esta pronto para disputar o Estadual! Desejem sorte aos nossos {len(time)} jogadores!"
    print(eValido)
else:
    naoValido = "Quem mandou ficar perdendo tempo com TikTok... Agora o Navegantes nao conseguira jogar o estadual :("
    print(naoValido)
