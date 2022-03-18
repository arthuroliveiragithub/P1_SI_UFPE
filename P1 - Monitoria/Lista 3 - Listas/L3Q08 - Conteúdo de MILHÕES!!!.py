n_entradas = int(input())
nomes_lifestyle = []
seguidores_lifestyle = []
views_lifestyle = []
nomes_utilidades = []
seguidores_utilidades = []
views_utilidades = []
nomes_dancinhas = []
seguidores_dancinhas = []
views_dancinhas = []
nome_famosinho, categoria_famosinho = '', ''
seguidores_famosinho = 0

while n_entradas > 0:
    nome, seguidores, views, categoria = input().split(", ")
    for letra in seguidores:
        if letra == "K":
            seguidores = seguidores.replace("K", "")
            seguidores = float(seguidores) / 1000
        if letra == "M":
            seguidores = seguidores.replace("M", "")
    for letra in views:
        if letra == "K":
            views = views.replace("K", "")
            views = float(views) / 1000
        if letra == "M":
            views = views.replace("M", "")
    if categoria == "Lifestyle":
        nomes_lifestyle.append(nome)
        seguidores_lifestyle.append(float(seguidores))
        views_lifestyle.append(float(views))
    if categoria == "Utilidades":
        nomes_utilidades.append(nome)
        seguidores_utilidades.append(float(seguidores))
        views_utilidades.append(float(views))
    if categoria == "Dancinhas":
        nomes_dancinhas.append(nome)
        seguidores_dancinhas.append(float(seguidores))
        views_dancinhas.append(float(views))
    if seguidores_famosinho < float(seguidores):
        nome_famosinho = nome
        seguidores_famosinho = float(seguidores)
        categoria_famosinho = categoria
    n_entradas -= 1

soma_lifestyle = 0
soma_utilidades = 0
soma_dancinhas = 0

for i in seguidores_lifestyle:
    soma_lifestyle += i
for i in seguidores_utilidades:
    soma_utilidades += i
for i in seguidores_dancinhas:
    soma_dancinhas += i

tamanho_lifestyle = len(nomes_lifestyle)
tamanho_utilidades = len(nomes_utilidades)
tamanho_dancinhas = len(nomes_dancinhas)

max_views_lifestyle, max_views_utilidades, max_views_dancinhas = 0, 0, 0
media_lifestyle, media_utilidades, media_dancinhas = 0, 0, 0

if tamanho_lifestyle > 0:
    media_lifestyle = soma_lifestyle / tamanho_lifestyle
    for i in range(tamanho_lifestyle):
        if views_lifestyle[i] > max_views_lifestyle:
            max_views_lifestyle = views_lifestyle[i]
if tamanho_utilidades > 0:
    media_utilidades = soma_utilidades / tamanho_utilidades
    for i in range(tamanho_utilidades):
        if views_utilidades[i] > max_views_utilidades:
            max_views_utilidades = views_utilidades[i]
if tamanho_dancinhas > 0:
    media_dancinhas = soma_dancinhas / tamanho_dancinhas
    for i in range(tamanho_dancinhas):
        if views_dancinhas[i] > max_views_dancinhas:
            max_views_dancinhas = views_dancinhas[i]

if tamanho_lifestyle > 0:
    print(f"Lifestyle;\nQuantidade de Tiktokers: {tamanho_lifestyle}\n"
          f"Media de seguidores: {media_lifestyle:.1f}M\nMaximo de visualizações: {max_views_lifestyle:.2f}M\n")
else:
    print(f"Lifestyle;\nNao foram informados dados sobre esta categoria.\n")
if tamanho_utilidades > 0:
    print(f"Utilidades;\nQuantidade de Tiktokers: {tamanho_utilidades}\n"
          f"Media de seguidores: {media_utilidades:.1f}M\nMaximo de visualizações: {max_views_utilidades:.2f}M\n")
else:
    print(f"Utilidades;\nNao foram informados dados sobre esta categoria.\n")
if tamanho_dancinhas > 0:
    print(f"Dancinhas;\nQuantidade de Tiktokers: {tamanho_dancinhas}\n"
          f"Media de seguidores: {media_dancinhas:.1f}M\nMaximo de visualizações: {max_views_dancinhas:.2f}M\n")
else:
    print(f"Dancinhas;\nNao foram informados dados sobre esta categoria.\n")

print(f"Os olhares do mundo estao sobre {nome_famosinho.upper()}, que conta com {seguidores_famosinho:.1f}M "
      f"de seguidores vendo seus videos diarios de {categoria_famosinho}!")
