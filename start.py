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

    # Create backProp
    backprop = backProp(2, 5, 2, 0.1)
    desired_output = None


    # Print initial state of backProp
    print_initial_state(backprop)
    print() # Adds a blank line

    ########## WILL NEED TO BE PUT INTO A FOR LOOP IN THE NEAR FUTURE
    for i in range(0,5):
        player_cards = [] # list of Player cards
        player_total = None
        dealer_cards = [] # list of Dealer cards
        dealer_total = None

        answers = [] # 0 for Draw, 1 for Hold; MAY DELETE
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
        # Converting the total (2 to 20) to a value between 0 to 1; Rounding to 5 decimal places
        '''NOTE: changed from (2 to 21) to (2 to 20) since 21 is not a possible player total; ace is only a 1 here'''
        inputs.append(round( (player_total - 1)/19.0 , 5))


        # Dealer draws 1 card
        dealerC1 = deck.get_deck().pop(0) # 49 cards left in deck
        # Add to list of Dealer cards
        dealer_cards.append(dealerC1)
        # Adding up the total points for the dealer
        dealer_total = dealerC1.get_value()
        # Converting the total (1 to 10) to a value between 0 to 1; Rounding to 5 decimal places
        inputs.append(round( (dealer_total - 1)/9.0 , 5))


        # Debug
        #print("DEBUG INFO")
        #print("len of pcards: %d" % len(player_cards))
        #print("len of dcards: %d" % len(dealer_cards))
        #print("pTotal: %s, dTotal: %s" % (player_total, dealer_total))
        #print("Inputs:", str(inputs))
        #print()

        # P's 1st card; P's 2nd card; D's 1st card; # of times
        ''' Will probably pass the player and dealer lists instead of the individual cards maybe... '''
        desired_output = runSimulation(deck, playerC1, playerC2, dealerC1, 10) # Returns 0 - draw or 1 -

        print(desired_output)

        line = "draw" if (desired_output == 0) else "hold"
        print("We want to %s" % line)

        print("")

        deck = None




##############START################

doit(1000000, 100000)

