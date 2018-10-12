# Usual python imports
import random

# Importing Classes, methods, etc from other files
# from [file] import [Class, method, etc]
from blackjack import runSimulation
from blackjack import Deck
from backprop import backProp # Imports the Class backProp so we can create an instance

'''
# To commit & push in pycharm
# 1) VCS>Commit...
# 2) VCS>Git>Push...
'''

def doit(epochs, showFrequency):
    backprop = backProp(2, 10, 2, 0.1)
    #print(backprop.get_weightBottoms())

    print("weight input (2) -> hiddens (10)")
    rows = len(backprop.get_weightBottoms())
    cols = 0
    if rows:
        cols = len(backprop.get_weightBottoms()[0])
    for j in range(rows):
        for i in range(cols):
                print("%8s " % (str(backprop.get_weightBottoms()[j][i])), end="")
        print()

    print()
    print("weight hiddens (10) -> outputs (2)")

    rows = len(backprop.get_weightTops())
    cols = 0
    if rows:
        cols = len(backprop.get_weightTops()[0])
    for j in range(rows):
        for i in range(cols):
            print("%8s " % (str(backprop.get_weightTops()[j][i])), end="")
        print()

    print()
    print("Bias for the hiddens")
    count = 1
    for i in backprop.get_biasBottom():
        print("%8s " % (str(i)), end="")
        if (count % 5) == 0:
            print()
        count += 1

    print()
    print("Bias for the outputs ")
    for i in backprop.get_biasTop():
        print("%8s " % (str(i)), end="")



##############START################

deck = Deck()

#print(deck)
#deck.shuffle_deck()

#shuffledDeck = deck.get_deck()

print("Five random cards")
for i in range(0, 10):
    deck.shuffle_deck()
    print("%d) %s" % (i + 1, deck.get_deck()[0]))

print("")

#print(decktemp[1])
#print(deck.get_deck()[1].get_name())
#print("%c" % (deck.get_deck()[0].get_name()[0]))

playerC1 = deck.get_deck()[0].get_name()
playerC2 = deck.get_deck()[1].get_name()
dealerC1 = deck.get_deck()[2].get_name()
print(playerC1, playerC2, dealerC1)

runSimulation()

#doit(1000000, 100000)

