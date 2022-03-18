
atualizacao_igual = "Nada mudou, a lista permanece igual"
lista_finalizada = "A lista ficou da seguinte forma:"
saida_erro = "Opçao não encontrada"
lista_convidados = []
entrada = ''
fim = False

while not fim:
    entrada = input()

    if entrada == "adicionar":
        nome_posicao = input().split()
        lista_convidados.insert(int(nome_posicao[1]), nome_posicao[0])
    elif entrada == "remover":
        nome = input()
        lista_convidados.remove(nome)
    elif entrada == "atualizar indice":
        nome_posicao = input().split()
        for i in range(len(lista_convidados)):
            if i == int(nome_posicao[1]):
                if lista_convidados[i] == nome_posicao[0]:
                    print(atualizacao_igual)
                else:
                    lista_convidados.remove(nome_posicao[0])
                    lista_convidados.insert(int(nome_posicao[1]), nome_posicao[0])
    elif entrada == "imprimir lista atual":
        print(" ".join(lista_convidados))
    elif entrada == "lista finalizada":
        print(lista_finalizada)
        print(" ".join(lista_convidados))
        fim = True
    else:
        print(saida_erro)
