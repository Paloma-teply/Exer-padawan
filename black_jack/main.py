from random import shuffle, random
from classes.baralho import Baralho

dict_baralho = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "A": '1 ou 11', "J": 10, "Q": 10, "K": 10}
baralho = [2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "J", "Q", "K"]

for k, v in dict_baralho.items():
    print(f'Carta: {k} Valor: {v}')
soma = 0
tem = 0
carta = None
while soma < 21:
    resposta = input("Gostaria de escolher outra carta? [S] ou [N]: ").upper()

    if resposta == 'S':
        shuffle(baralho)
        carta = baralho[0]

        if tem == 0 and carta == 'A':
            carta = 11
            soma += carta
            print(carta)

        elif tem != 0:
            if carta == 'A':
                carta = 1
                soma += carta
                print(carta)

        if str(carta) in 'JQK':
            carta = 10
            soma += carta
            print(carta)
        
        else:
            soma += carta
            print(carta)

        tem = 1
    elif resposta == 'N':
        break

    if soma == 21:
        print('voce venceu')
        break
    elif soma > 21:
        print('voce perdeu')
        break
