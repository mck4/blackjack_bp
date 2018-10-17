'''
Programmed by Zoey Abrigo and Carolina Kimbrough

start.py
This is where we invoke the function, doit, to start the whole program.
'''

# Usual python imports
import random

# Importing Classes, methods, etc from other files
# from [file] import [Class, method, etc]
from blackjack import runSimulation1    # blackjack.py
from blackjack import runSimulation2
from blackjack import Deck
from backprop import backProp           # backprop.py
from backprop import predictBP
from backprop import adjustWeights
from print import print_initial_state   # print.py
from print import print_prediction


# Function which starts the whole program
def doit(epochs, showFrequency):

    # Create backProp
    backprop1 = backProp(2, 7, 2, 0.01)
    backprop2 = backProp(2, 7, 2, 0.01)

    # BP1
    num_right = 0  # Number of guesses right
    num_wrong = 0  # Number of guesses wrong

    # BP2
    num_wrong2 = 0 # Number of guesses right
    num_right2 = 0 # Number of guesses wrong

    # PRINT INITIAL STATE
    print("\n______________________INITIAL STATE OF NETWORK________________________")
    print("INITIAL STATE FOR 2 CARDS\n")
    # Print initial state of backProp
    print_initial_state(backprop1)
    print() # Adds a blank line

    print("INITIAL STATE FOR 3 CARDS\n")
    # Print initial state of backProp
    print_initial_state(backprop2)
    print()  # Adds a blank line

    # Loop through the epochs
    for i in range(1, epochs + 1):
        player_cards = []    # list of Player cards
        player_total = None  # player total value
        dealer_cards = []    # list of Dealer cards
        dealer_total = None  # dealer total value

        guess = None         # a guess
        confidence = None    # confidence in guess
        percent = None       # percentage right

        # Two inputs: Player's total, Dealer's total
        inputs1 = []    # BP1

        # Initialize deck
        deck = Deck()   # BP1 and BP2 share this deck

        # Shuffle deck
        deck.shuffle_deck()

        # Player draws 2 cards
        playerC1 = deck.deck.pop(0) # 51 cards left in deck
        playerC2 = deck.deck.pop(0) # 50 cards left in deck
        # Add to list of Player cards
        player_cards.append(playerC1)
        player_cards.append(playerC2)
        # Adding up the total points for the player
        player_total = playerC1.value + playerC2.value
        # Converting the total (2 to 21) to a value between 0 to 1
        inputs1.append((player_total - 2)/19.0)


        # Dealer draws 1 card
        dealerC1 = deck.deck.pop(0) # 49 cards left in deck
        # Add to list of Dealer cards
        dealer_cards.append(dealerC1)
        # Adding up the total points for the dealer
        dealer_total = dealerC1.value
        # Converting the total (1 to 10) to a value between 0 to 1
        inputs1.append((dealer_total - 1)/9.0)


        # P's 1st card; P's 2nd card; D's 1st card; # of times
        desired_output1 = runSimulation1(deck, playerC1, playerC2, dealerC1, 50, i) # Returns 0 - draw or 1 - hold

        # Get a guess and the confidence
        (guess, confidence) = predictBP(backprop1, inputs1)


        # Update right/wrong counter
        if guess == desired_output1:
            num_right += 1
        else:
            num_wrong += 1

        # For printing; did we hold or draw?
        desired_line = "draw" if (desired_output1 == 0) else "hold"
        guess_line = "draw" if (guess == 0) else "hold"

        # Comes after runSimulation because we use the desired_output to calculate other stuff
        # Print first 10 epochs & then every value of showFrequency thereafter
        if(i <= 10 or ((i % showFrequency) == 0)):
            percent = (100.0 * num_right) / (num_right + num_wrong)
            print("%d.  (%s %s - % s) -> %s with conf=%.5f desired=%s right=%.2f%s\t BP1" %
                  (i , playerC1.name, playerC2.name, dealerC1.name, guess_line, confidence, desired_line, percent, "%"))

            '''
            if(i <= 5 or (i == epochs)):
                print()
                print_prediction(backprop1, inputs1)
                print()
            '''

        # Adjust the weights for BP1
        adjustWeights(backprop1, inputs1, desired_output1)

        # If the guess is to draw, invoke BP2
        if guess is 0:

            # Two inputs: Player's total, Dealer's total
            inputs2 = [] # Special for BP2

            # Player draws 1 more card, the 3rd card
            playerC3 = deck.deck.pop(0)  # at least 4 less cards left in deck
            # Add to list of Player cards
            player_cards.append(playerC3)
            # Adding up the total points for the player
            player_total = playerC1.value + playerC2.value + playerC3.value
            # Converting the total (2 to 21) to a value between 0 to 1
            inputs2.append((player_total - 2) / 19.0)


            # Converting the total (1 to 10) to a value between 0 to 1
            inputs2.append((dealer_total - 1) / 9.0)


            # P's 1st card; P's 2nd card; D's 1st card; # of times
            # Special for BP2
            desired_output2 = runSimulation2(deck, playerC1, playerC2, playerC3, dealerC1, 50, i)  # Returns 0 - draw or 1 - hold

            # Get a guess and the confidence
            (guess2, confidence) = predictBP(backprop2, inputs2)


            # Update right/wrong counter for BP2
            if guess2 == desired_output2:
                num_right2 += 1
            else:
                num_wrong2 += 1

            # For printing; did we hold or draw?
            desired_line = "draw" if (desired_output2 == 0) else "hold"
            guess_line = "draw" if (guess2 == 0) else "hold"

            # Comes after runSimulation because we use the desired_output to calculate other stuff
            # Print first 10 epochs & then every value of showFrequency thereafter
            # Special for BP2, three cards displayed now
            if (i <= 10 or ((i % showFrequency) == 0)):
                percent2 = (100.0 * num_right2) / (num_right2 + num_wrong2)
                print("%d.  (%s %s %s - % s) -> %s with conf=%.5f desired=%s right=%.2f%s\t BP2\n" %
                      (i, playerC1.name, playerC2.name, playerC3.name, dealerC1.name, guess_line, confidence, desired_line, percent2,
                       "%"))
                '''
                if (i <= 5 or (i == epochs)):
                    print()
                    print_prediction(backprop2, inputs2)
                    print()
                '''
            # Adjust the weights for BP1
            adjustWeights(backprop2, inputs2, desired_output2)

    # PRINT FINAL NETWORK #
    print("______________________FINAL STATE OF THE NETWORK________________________")
    print("FINAL STATE FOR 2 CARDS\n")
    # Print initial state of backProp
    print_initial_state(backprop1)
    print()  # Adds a blank line

    print("FINAL STATE FOR 3 CARDS\n")
    # Print initial state of backProp
    print_initial_state(backprop2)
    print()  # Adds a blank line

##############START################

print()
doit(200000, 10000) # Start!

