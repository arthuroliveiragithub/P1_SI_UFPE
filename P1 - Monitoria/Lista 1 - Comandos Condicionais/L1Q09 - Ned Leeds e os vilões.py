# https://www.dikastis.com.br/problems/01FV4DDWFMYACNCKCCSGW1C0GH

nome_vilao_1 = input()
poder_vilao_1 = int(input())
local_vilao_1 = int(input())
nome_vilao_2 = input()
poder_vilao_2 = int(input())
local_vilao_2 = int(input())

destruicao_1 = ((poder_vilao_1**2) * local_vilao_1)/2
destruicao_2 = ((poder_vilao_2**2) * local_vilao_2)/2

if destruicao_1 <= 0 or destruicao_2 <= 0:
    print("Nem faco essa comparacao! Quero ser um vingador, busco coisas maiores.")
elif destruicao_1 >= destruicao_2 and destruicao_1 > 0:
    if destruicao_1 == destruicao_2:
        if destruicao_1 % 2 == 0:
            print("E quem disse que isso e problema meu? Vou chamar o senhor Stark.")
        else:
            print("Vou chamar uns reforcos de outro universo... rsrs")
    else:
        print(f"Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {nome_vilao_1}.")
else:
    print(f"Com grandes poderes, vem grandes responsabilidades. Com isso, preciso ir deter o {nome_vilao_2}.")
