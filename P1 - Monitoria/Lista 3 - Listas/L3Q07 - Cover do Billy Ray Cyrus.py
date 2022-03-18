musica = []
ruidos = 0

for i in range(10):
    verso = input().split()
    if verso[0] == "tss" or verso[0] == "zzz":
        verso.remove(verso[0])
        ruidos += 1
    if len(verso) > 1:
        if verso[-1] == "tss" or verso[-1] == "zzz":
            verso.remove(verso[-1])
            ruidos += 1
    if verso:
        verso = " ".join(verso)
        musica.append(verso)

musica_completa = "\n".join(musica)

if len(musica) >= 8 and 0 < ruidos <= 4:
    mensagem = "Todo o ruido foi removido e voce mandou bem! A legenda saiu certinha. Pode subir!"
elif len(musica) < 8 or ruidos > 4:
    mensagem = "Ih, tem alguma coisa errada com a legenda, ta estranha. Melhor dar uma verificada e regravar."
else:
    mensagem = "Nem precisava rodar, o audio ja estava limpinho e a legenda ta nos conformes. Marca o @billyraycyrus"

if musica_completa:
    print("Legenda final:\n\n", musica_completa, "\n\n", mensagem)
else:
    print("Eita, a legenda simplesmente inexiste! Tudo era ruido!")
