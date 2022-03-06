# https://www.dikastis.com.br/problems/01FW9V9CYD6B6X6Y3FBFY8VAQE

local_desejado = int(input())
progresso = int(input())
output = ''
soma = 0

while progresso >= 0:
    contador = 1
    while contador <= progresso:
        soma += contador
        contador += 1
    progresso = int(input())

if soma < local_desejado:
    output = "Ainda nos falta um pouco..."
elif soma == local_desejado:
    output = "Pode beijar a noiva, afinal, vocês conseguiram!"
elif local_desejado < soma < (20 * local_desejado):
    output = "Parece que os pombinhos passaram um pouco do local..."
elif (20 * local_desejado) <= soma <= (100 * local_desejado):
    output = "Acho que nos perdemos um pouco no caminho, onde estamos?"
elif soma > (100 * local_desejado):
    output = "Hum... acho que o casal deve rever seus votos de matrimônio..."

print(output)
