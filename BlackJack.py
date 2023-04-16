import random
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

    random.shuffle(deck)
    return deck


def main():

    try:
        with open('money.txt', 'r') as f:
            player_money = float(f.readline())
    except FileNotFoundError:

        player_money = Max_Bet

    print("Welcome to BLACK JACK!")
    player_bet = float(input("How much would you like to bet? "))

    if player_bet < Min_Bet or player_bet > player_money:
        print("Invalid bet amount. The minimum bet you can enter is 5")
        return


    player_money -= player_bet
    deck = Deck_Card()
    dealer_hand, player_hand = Playing_Card(deck)

    player_hand_total = Black_Jack_Hand(player_hand)
    dealer_hand_total = Black_Jack_Hand(dealer_hand)

    while Black_Jack_Hand(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
        print("Dealer draws a card")

    if player_hand_total == 21:
        print("Congratulations! You have a blackjack!")
        player_money += round(player_bet * 1.5, 2)
        print("Your balance is", player_money)
    elif dealer_hand_total == 21:
        print("Dealer won! You lose.")
        player_money -= player_bet
        print("Your balance", player_money)
    else:
        while Black_Jack_Hand(player_hand) < 21:
            action = input ("Hit or stand? (hit/stand) ")
            if action == 'hit':
                player_hand.append(deck.pop())
                print("Your cards:", player_hand)
            elif action == 'stand':
                break

        if dealer_hand_total > 21:
            print("Dealer busts!")
            player_money += round(player_bet * 2, 2)
        elif player_hand_total > dealer_hand_total:
            print("Player wins!")
            player_money += round(player_bet * 2, 2)
        elif player_hand_total == dealer_hand_total:
            print("It is a tie!")
            player_money += player_bet
            print("Your balance is", player_money)



    with open('money.txt', 'w') as f:
        f.write(str(player_money))

    play_again = input("Do you want to play again? (y/n) ")
    if play_again.lower() == "y":
        main()

if __name__ == '__main__':
    main()