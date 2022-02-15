arma = int(input())

if arma % 2 == 0:
    tipo_arma = "cortante"
else:
    tipo_arma = "atordoante"

if arma == 1:
    print("A arma corpo a corpo escolhida foi: Cassetete")
    print(f"A arma corpo a corpo escolhida e {tipo_arma}")
elif arma == 2:
    print("A arma corpo a corpo escolhida foi: Garrafa de Whisky")
    print(f"A arma corpo a corpo escolhida e {tipo_arma}")
elif arma == 3:
    print("A arma corpo a corpo escolhida foi: Soco Ingles")
    print(f"A arma corpo a corpo escolhida e {tipo_arma}")
elif arma == 4:
    print("A arma corpo a corpo escolhida foi: Lamina Escondida")
    print(f"A arma corpo a corpo escolhida e {tipo_arma}")
elif arma == 5:
    print("A arma corpo a corpo escolhida foi: Pe de Cabra")
    print(f"A arma corpo a corpo escolhida e {tipo_arma}")
elif arma == 6:
    print("A arma corpo a corpo escolhida foi: Canivete")
    print(f"A arma corpo a corpo escolhida e {tipo_arma}")
elif arma < 1 or arma > 6:
    print("Numero invalido")
