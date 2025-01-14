

def score():
    vit = int(input('Digite o número de suas vitórias: '))
    lose = int(input('Digite o número de suas derrotas: '))
    score = vit - lose
    return score 


def rank_calculator():
    rank = score()  
    if rank < 10:
        nivel = "Ferro"
    elif 10 <= rank <= 20:
        nivel = "Bronze"
    elif 21 <= rank <= 50:
        nivel = "Prata"
    elif 51 <= rank <= 80:
        nivel = "Ouro"
    elif 81 <= rank <= 90:
        nivel = "Diamante"
    elif 91 <= rank <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"
    
    return nivel 

vitorias = score()
resultado = rank_calculator()


print(f"O Herói tem {vitorias} vitórias e está no nível de {resultado}")
