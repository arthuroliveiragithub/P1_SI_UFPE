# dikastis.com.br/problems/01FW9R300CG22T943RRNVM70Z3

acidez = 20
agua = 15
tempero = 10
fim = False

while not fim:
    n = int(input())
    acao = input()

    if acao == "reduzir agua":
        agua -= n
        tempero += (n-1)
    elif acao == "adicionar agua":
        agua += n
        tempero -= (n+2)
    elif acao == "reduzir acidez":
        acidez -= n
    elif acao == "aumentar acidez":
        acidez += n
    elif acao == "aumentar tempero":
        tempero += n

    if acidez == agua == tempero:
        print("Tem sabor, tem apresentacion, tem tudibon! sobe no mezanin")
        fim = True
    else:
        menor = min(acidez, agua, tempero)
        if menor == agua:
            print("Muit seca! melhorre a combinaçon")
        if menor == tempero:
            print("Falta tomperro! non agradou meu paladar")
        if menor == acidez:
            print("Falta acidez! non pode subir o mezanin")
