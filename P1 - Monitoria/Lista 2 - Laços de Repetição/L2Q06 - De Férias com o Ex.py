# https://www.dikastis.com.br/problems/01FWA6H5WGQ9DGM7XV8DPW78AG

total_cerveja = 0
total_caipirinha = 0
total_vodca = 0

n_festas = int(input())
cont_festas = 0
while cont_festas < n_festas:
    n_copos = int(input())
    cont_copos = 0
    n_cerveja = 0
    n_caipirinha = 0
    n_vodca = 0
    maior_bebida = ""
    n_maior_bebida = 0

    while cont_copos < n_copos:
        bebida = input()
        if bebida == "cerveja":
            n_cerveja += 1
            total_cerveja += 1
        elif bebida == "caipirinha":
            n_caipirinha += 1
            total_caipirinha += 1
        elif bebida == "vodca":
            n_vodca += 1
            total_vodca += 1
        cont_copos += 1

    if n_cerveja > n_maior_bebida:
        n_maior_bebida = n_cerveja
        maior_bebida = "cerveja"
    if n_caipirinha > n_maior_bebida:
        n_maior_bebida = n_caipirinha
        maior_bebida = "caipirinha"
    if n_vodca > n_maior_bebida:
        n_maior_bebida = n_vodca
        maior_bebida = "vodca"

    output = f"O que ele mais tomou nessa festa foi: {maior_bebida}"
    print(output)
    cont_festas += 1

output = f"cerveja - {total_cerveja}\n"\
        f"caipirinha - {total_caipirinha}\n"\
        f"vodca - {total_vodca}"
print(output)
