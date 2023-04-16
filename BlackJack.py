Min_Bet = 5
Max_Bet = 1000

def Black_Jack_Hand(hand):
    total = 0
    ace_count = sum(card[0] == 'Ace' for card in hand)

    for i in range(ace_count):
        if total + 11 <= 21:
            total += 11
        else:
            total +=1
    for card in hand:
        if card[0] != 'Ace':
            total += card [1]
    return total
def Playing_Card(deck):
    dealer_hand = []
    player_hand = []

    for i in range (2):
        dealer_hand.append(deck.pop())
        player_hand.append(deck.pop())
    print("Dealer's hand:", dealer_hand[0])
    print("Player's hand:", player_hand)
    return dealer_hand, player_hand

def Deck_Card():
    deck = []
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    points = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

    for suit in suits:
        for rank in ranks:
            card = [rank + ' of ' + suit]
            deck.append(card)
    return deck


def main():
    print("Welcome to BLACK JACK!")
    player_bet = float(input("How much would you like to bet? "))
    if player_bet < Min_Bet or player_bet > Max_Bet:
        print("Invalid bet amount. The minimum bet you can enter is 5")
    player_money = Max_Bet
    player_money -= player_bet
    deck = Deck_Card()
    dealer_hand, player_hand = Playing_Card(deck)
    player_hand_total = Black_Jack_Hand(player_hand)
    dealer_hand_total = Black_Jack_Hand(dealer_hand)
    print("Player's total:", player_hand_total)

if __name__ == '__main__':
    main()