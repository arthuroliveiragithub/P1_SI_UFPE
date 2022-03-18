hashtags = ["ABCDEFGHIJKLMNOPQRSTUVXWYZ"]
qtd_hashtags = int(input())

for i in range(qtd_hashtags):
    temMaiuscula = False
    hashtag = input()
    for letra in hashtag:
        for maiuscula in hashtags[0]:
            if letra == maiuscula:
                temMaiuscula = True
    if not temMaiuscula:
        hashtags.append(hashtag)

for i in range(1, len(hashtags)):
    for j in range(1, len(hashtags) - 1):
        if hashtags[j] > hashtags[j+1]:
            hashtags[j], hashtags[j+1] = hashtags[j+1], hashtags[j]

for i in range(1, len(hashtags)):
    print(hashtags[i])
