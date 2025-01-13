


hero = input("nome do seu heroi: ")
xp = int(input("quantidade de xp: "))
nivel = ()


if xp < 1000:
    nivel = "Ferro"
    print(nivel)
elif xp >= 1001 and xp <= 2000 :
    nivel = "Bronze"
    print(nivel)
elif xp >= 2001 and xp <= 5000:
    nivel = "Prata"
    print(nivel)
elif xp >= 6001 and xp <= 7000:
    nivel = "Ouro"
    print(nivel)
elif xp >= 7001 and xp <= 8000:
    nivel = "Platina"
    print(nivel)
elif xp >= 8001 and xp <= 9000:
    nivel = "Ascendente"
    print(nivel)
elif xp >= 9001 and xp <= 10000:
    nivel = "Imortal"
    print(nivel)
elif xp >= 10001:
    nivel = "Radiante"
    print(nivel)


print("Héroi: ", hero, " esta no nivel de ", nivel )

