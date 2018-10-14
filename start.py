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

    backprop = backProp(2, 5, 2, 0.1) # Create backprop
    player_cards = [] # list of Player cards
    player_total = None
    dealer_cards = [] # list of Dealer cards
    dealer_total = None

    # Initialize deck
    deck = Deck()

    # Shuffle deck
    deck.shuffle_deck()

    # Player draws 2 cards
    playerC1 = deck.get_deck().pop(0)
    playerC2 = deck.get_deck().pop(0)
    # Add to list of Player cards
    player_cards.append(playerC1)
    player_cards.append(playerC2)
    player_total = playerC1.get_value() + playerC2.get_value()

    # Dealer draws 1 card
    dealerC1 = deck.get_deck().pop(0)
    # Add to list of Dealer cards
    dealer_cards.append(dealerC1)
    dealer_total = dealerC1.get_value()

    print(player_total, dealer_total)

    # P's 1st card; P's 2nd card; D's 1st card; # of times
    runSimulation(deck, playerC1, playerC2, dealerC1, 20)

    print("")
    print_initial_state(backprop)



##############START################

doit(1000000, 100000)

