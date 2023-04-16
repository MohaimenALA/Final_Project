Min_Bet = 5
Max_Bet = 1000

def Black_Jack_Hand():
    total = 0
    aceCount = 0


def Playing_Card():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    points = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}
    for suit in suits:
        for rank in ranks:
            card = [rank + ' of ' + suit, points[rank]]
            deck.append(card)
def main():
    print("Welcome to BLACK JACK!")
    player_bet = input("How much would you like to bet? ")
    if player_bet < Min_Bet or player_bet > Max_Bet:
        print("Invalid bet amount. The minimum bet you can enter is 5")

    player_money -= player_bet

if __name__ == '__main__':
    main()