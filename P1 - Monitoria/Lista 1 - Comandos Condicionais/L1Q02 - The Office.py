nome = input()
valor_sem1 = int(input())
valor_sem2 = int(input())

media_mensal = int((valor_sem1 + valor_sem2)/12)

if nome == "Jim Halpert" or nome == "Dwight Schrute" or nome == "Phyllis Vance" or nome == "Stanley Hudson":
    if media_mensal <= 50:
        print(f'{nome}, voce so vendeu {media_mensal} por mes? Voce ta demitido... Brincadeira!')
    elif 50 < media_mensal < 100:
        print(f'{nome}, voce mandou mal... Vai ter que pagar meu almoco.')
    else:
        print(f'Parabens, {nome}! Voce foi promovido! kkkkk Brincadeira, a matriz que decide!')
else:
    print('Sinto muito, mas so os vendedores eh que vao ganhar a viagem pra matriz.')