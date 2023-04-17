import csv
from db import read_money_amount, write_money_amount
import random


SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
RANKS = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
VALUES = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "Jack": 10, "Queen": 10, "King": 10}


def get_bet_amount(player_money):
    """
    Asks the player for the bet amount and returns the bet amount
    """
    while True:
        try:
            bet_amount = float(input(f"Enter your bet amount (you have {player_money}$): "))
            if bet_amount <= 0:
                print("Bet amount must be greater than zero.")
            elif bet_amount > player_money:
                print("You don't have enough money to make this bet.")
            else:
                return bet_amount
        except ValueError:
            print("Invalid input. Please enter a valid bet amount.")


def get_card(deck):
    """
    Draws a card from the deck and returns the card
    """
    return deck.pop()


def deal_initial_hands(deck, dealer_hand, player_hand):
    """
    Deals two cards to the dealer and two cards to the player
    """
    for _ in range(2):
        dealer_hand.append(get_card(deck))
        player_hand.append(get_card(deck))


def display_hands(dealer_hand, player_hand, show_dealer_hand=False):
    """
    Displays the dealer's and player's hands
    """
    print("\nDealer's Hand:")
    if show_dealer_hand:
        for card in dealer_hand:
            print(f"  {card[0]} of {card[1]}")
    else:
        print(f"  {dealer_hand[0][0]} of {dealer_hand[0][1]}")
        print("  <card hidden>")

    print("\nPlayer's Hand:")
    for card in player_hand:
        print(f"  {card[0]} of {card[1]}")
    print("")


def player_turn(deck, dealer_hand, player_hand):
    """
    Allows the player to draw cards until they stand or bust
    """
    while True:
        action = input("Do you want to Hit or Stand? ").lower()
        if action == "hit":
            player_hand.append(get_card(deck))
            display_hands(dealer_hand, player_hand)
            if get_hand_value(player_hand) > 21:
                print("Bust! You lose.")
                return "bust"
        elif action == "stand":
            return "stand"
        else:
            print("Invalid input. Please enter Hit or Stand.")


def dealer_turn(deck, dealer_hand):
    """
    Allows the dealer to draw cards until they have at least 17 points or bust
    """
    while get_hand_value(dealer_hand) < 17:
        dealer_hand.append(get_card(deck))
        display_hands(dealer_hand, player_hand, show_dealer_hand=True)
        if get_hand_value(dealer_hand) > 21:
            print("Dealer busts! You win.")
            return "dealer bust"
    return "stand"


def get_hand_value(hand):
    """
    Calculates the value of a hand and returns the value
    """
    # Calculate the total value of the hand
    value = sum(VALUES[card[0]] for card in hand)

    # If the hand has an Ace and the total value is greater than 21, reduce the value of the Ace from 11 to 1
    num_aces = sum(1 for card in hand if card[0] == "Ace")
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1

    return value


def payout(player_hand, dealer_hand, bet_amount):
    """
    Calculates the payout for the player and updates the player's money amount
    """
    player_hand_value = get_hand_value(player_hand)
    dealer_hand_value = get_hand_value(dealer_hand)

    if player_hand_value == 21 and len(player_hand) == 2:
        print("Blackjack! You win.")
        payout_amount = bet_amount * 1.5
    elif dealer_hand_value > 21:
        print("Dealer busts! You win.")
        payout_amount = bet_amount
    elif player_hand_value > dealer_hand_value:
        print("You win.")
        payout_amount = bet_amount
    elif player_hand_value < dealer_hand_value:
        print("You lose.")
        payout_amount = -bet_amount
    else:
        print("Push.")
        payout_amount = 0

    return payout_amount


def main():
    # Read the player's money amount from the file
    player_money = read_money_amount()
    print("Welcome to BlackJack")
    print()
    while True:
        # Check if the player has enough money to play
        if player_money < 5:
            print("You don't have enough money to make the minimum bet. Please buy more chips.")
            buy_chips = input("Do you want to buy chips? (y/n) ").lower()
            if buy_chips == "y":
                player_money += 100
                write_money_amount(player_money)
            else:
                break

        # Get the bet amount from the player
        bet_amount = get_bet_amount(player_money)

        # Create the deck of cards
        deck = []
        for suit in SUITS:
            for rank in RANKS:
                deck.append([rank, suit])

        # Shuffle the deck
        random.shuffle(deck)

        # Deal the initial hands
        dealer_hand = []
        player_hand = []
        deal_initial_hands(deck, dealer_hand, player_hand)

        # Display the hands
        display_hands(dealer_hand, player_hand)

        # Player's turn
        player_result = player_turn(deck, dealer_hand, player_hand)

        # Dealer's turn
        if player_result != "bust":
            dealer_result = dealer_turn(deck, dealer_hand)
        else:
            dealer_result = ""

        # Payout
        if dealer_result != "dealer bust":
            payout_amount = payout(player_hand, dealer_hand, bet_amount)
            player_money += payout_amount
            write_money_amount(player_money)

        # Display the hands again with the dealer's hand revealed
        display_hands(dealer_hand, player_hand, show_dealer_hand=True)

        # Check if the player wants to play again
        play_again = input(f"You have {player_money}$. Do you want to play again? (y/n) ").lower()
        if play_again != "y":
            break
        print("bye!")

if __name__ == "__main__":
    main()