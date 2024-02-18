############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from os import system, name
from random import choice
from art import logo

# Deck of cards.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# This fuction clears the screen.
def clear():
  # For Windows.
  if name == 'nt':
    _ = system('cls')
  # for mac and linux(here, os.name is 'posix'
  else: 
    _ = system('clear')


# This function returns the starting hand.
def deal_starting_cards(hand):
  for _ in range(2):
    card = choice(cards)
    hand.append(card)


# This function deals the cards to the input hand.
def deal_hand(hand):
  hand.append(choice(cards))


# This function check if there is a black jack in the hand.
def is_blackjack(hand):
  if len(hand) == 2 and sum(hand) == 21 and (hand[0] == 11 or hand[1] == 11):
    return True
  return False


# This function calculate scores.
# If an ace is drawn, count it as 11,
# But if the total goes over 21, count the ace as 1 instead.
def calculate_score(hand):
  score = sum(hand)
  if 11 in hand and score > 21:
    hand.remove(11)
    hand.append(1)
    score = sum(hand)
  return score


#
def print_player_hand(player_hand, dealer_hand):
  print(f"\n\tYour cards: {player_hand}")
  print(f"\tYour score: {calculate_score(player_hand)}\n")
  print(f"\tDealer's first card: {dealer_hand[0]}")


def print_dealer_hand(dealer_hand):
  print(f"\n\tDealers cards: {dealer_hand}")
  print(f"\tDealer score: {calculate_score(dealer_hand)}\n")


def print_both_hands(player_hand, dealer_hand):
  print(f"\n\tYour cards: {player_hand}")
  print(f"\tYour score: {calculate_score(player_hand)}\n")
  print(f"\n\tDealers cards: {dealer_hand}")
  print(f"\tDealer score: {calculate_score(dealer_hand)}\n")


def blackjack():
  player_hand = []
  dealer_hand = []
  player_turn = 'y'
  player_bust = False
  dealer_bust = False

  deal_on = True
  while deal_on:
    print(logo)

    # Staring the deal.
    deal_starting_cards(player_hand)
    deal_starting_cards(dealer_hand)
    print_player_hand(player_hand, dealer_hand)

    # Check if the player has blackjack.
    if is_blackjack(player_hand):
      print("\n\tYou got blackjack. You Win!!")

    elif is_blackjack(dealer_hand):
      print("\n\tDealer has blackjack. You lose.")

    else:

      while player_turn == "y" and not player_bust:

        player_turn = input("Type 'y' to Hit, type 'n' to Pass: ")
        if player_turn == 'n':
          break

        deal_hand(player_hand)
        print_player_hand(player_hand, dealer_hand)
        player_score = calculate_score(player_hand)
        if player_score > 21:
          print("\n\tYou busted. You lose.")
          player_bust = True

      if not player_bust and player_turn == "n":
        print_both_hands(player_hand, dealer_hand)
        dealer_score = calculate_score(dealer_hand)
        while dealer_score < 17 and not dealer_bust:
          deal_hand(dealer_hand)
          print_dealer_hand(dealer_hand)
          dealer_score = calculate_score(dealer_hand)
          if dealer_score > 21:
            print("\n\tDealer busted. You win!!")
            dealer_bust = True

      if not player_bust and not dealer_bust:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        print_both_hands(player_hand, dealer_hand)
        if player_score > dealer_score:
          print("\n\tYou Win!!")
        elif dealer_score > player_score:
          print("\n\tYou lose.")
        else:
          print("\n\tIt's a Push!")

    player_input = input(
        "\nDo you want to play a game of Blackjack? Type 'y' or 'n': ")
    if player_input == "y":
      clear()
      player_hand = []
      dealer_hand = []
      player_turn = 'y'
      player_bust = False
      dealer_bust = False
    else:
      deal_on = False


blackjack()
