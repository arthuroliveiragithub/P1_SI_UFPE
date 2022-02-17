arma = int(input())
nome_arma = ''

if arma % 2 == 0:
    tipo_arma = "cortante"
else:
    tipo_arma = "atordoante"

if arma == 1:
    nome_arma = "Cassetete"
elif arma == 2:
    nome_arma = "Garrafa de Whisky"
elif arma == 3:
    nome_arma = "Soco Ingles"
elif arma == 4:
    nome_arma = "Lamina Escondida"
elif arma == 5:
    nome_arma = "Pe de Cabra"
elif arma == 6:
    nome_arma = "Canivete"
elif arma < 1 or arma > 6:
    print("Numero invalido")

if nome_arma != '':
    print(f"A arma corpo a corpo escolhida foi: {nome_arma}")
    print(f"A arma corpo a corpo escolhida e {tipo_arma}")
