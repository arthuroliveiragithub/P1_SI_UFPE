lista_likes = []
usuario_com_mais_likes = ''
mais_likes = 0

qtd_videos = int(input())
for i in range(qtd_videos):
    usuario = input()
    likes = int(input())
    if likes > mais_likes:
        usuario_com_mais_likes = usuario
        mais_likes = likes
    lista_likes.append(likes)

print(lista_likes)

for i in range(len(lista_likes)):
    for j in range(len(lista_likes) - 1):
        if lista_likes[j] < lista_likes[j+1]:
            lista_likes[j], lista_likes[j+1] = lista_likes[j+1], lista_likes[j]

print(lista_likes)

print("O numero de curtidas dos videos que vao aparecer na For You segue a ordem:")
for i in range(len(lista_likes)):
    if i != (len(lista_likes) - 1):
        print(lista_likes[i], end=", ")
    else:
        print(lista_likes[i])
print(f"O primeiro usuario que vai aparecer na For You e {usuario_com_mais_likes}!")
