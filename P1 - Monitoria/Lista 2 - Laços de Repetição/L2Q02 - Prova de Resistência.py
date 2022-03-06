# https://www.dikastis.com.br/problems/01FTTN33CNENZNWKERVAFDBX9K

n_sairam = int(input())
emparedado = ''
ganhador = ''
frase = ''
contador = 0
while contador < n_sairam:
    nome_eliminado = input()
    frase = ''

    if contador == 0:
        emparedado = nome_eliminado
    elif contador == 18:
        ganhador = nome_eliminado

    if nome_eliminado == "Prior":
        frase = "IIIHHH! El mago esta eliminado!"
    elif nome_eliminado == "Manu":
        frase = "Manu saiu! Bruna Marquezine deve estar muito triste :("
    elif nome_eliminado == "Pyong":
        frase = "Agora o Pyong que dormiu, esta eliminado"
    elif nome_eliminado == "Gizelly":
        frase = "PPPPPYYYYYOOOONNNGGG LEEEEEE, Gizelly volta pra casa!"
    if frase != '':
        print(frase)
    contador += 1

if n_sairam < 19:
    frase = f"- Ainda restam {19 - n_sairam} pessoas na disputa pela lideranca!"
elif n_sairam == 19:
    frase = f"- O novo lider da semana e: {ganhador}!"

print(f"- O indicado(a) ao paredao nessa semana e: {emparedado}")
print(frase)
