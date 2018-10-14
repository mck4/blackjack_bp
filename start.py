# Usual python imports
import random

# Importing Classes, methods, etc from other files
# from [file] import [Class, method, etc]
from blackjack import runSimulation
from blackjack import Deck
from backprop import backProp # Imports the Class backProp so we can create an instance
from print import print_initial_state

'''
# To commit & push in pycharm
# 1) VCS>Commit...
# 2) VCS>Git>Push...
'''

def doit(epochs, showFrequency):

    backprop = backProp(2, 5, 2, 0.1) # Create

    print_initial_state(backprop)
    print()

    player_cards = [] # list of Player cards
    player_total = None
    dealer_cards = [] # list of Dealer cards
    dealer_total = None

    inputs = [] # Two inputs: Player's total, Dealer's total

    # Initialize deck
    deck = Deck()

    # Shuffle deck
    deck.shuffle_deck()

    # Player draws 2 cards
    playerC1 = deck.get_deck().pop(0) # 51 cards left in deck
    playerC2 = deck.get_deck().pop(0) # 50 cards left in deck
    # Add to list of Player cards
    player_cards.append(playerC1)
    player_cards.append(playerC2)
    # Adding up the total points for the player
    player_total = playerC1.get_value() + playerC2.get_value()
    # Converting the total (2 to 21) to a value between 0 to 1
    inputs.append((player_total - 1)/19.0) #NOTE: maybe the total is 2 to 20??

    # Dealer draws 1 card
    dealerC1 = deck.get_deck().pop(0) # 49 cards left in deck
    # Add to list of Dealer cards
    dealer_cards.append(dealerC1)
    # Adding up the total points for the dealer
    dealer_total = dealerC1.get_value()
    # Converting the total (1 to 10) to a value between 0 to 1
    inputs.append((dealer_total - 1)/9.0)

    # Debug
    print(player_total, dealer_total)
    print(inputs)

    # P's 1st card; P's 2nd card; D's 1st card; # of times
    runSimulation(deck, playerC1, playerC2, dealerC1, 20)

    print("")




##############START################

doit(1000000, 100000)

