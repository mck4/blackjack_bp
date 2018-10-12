# Usual python imports
import random

# Importing Classes, methods, etc from other files
# from [file] import [Class, method, etc]
from blackjack import blackjack_print
from backprop import backProp # Imports the Class backProp so we can create an instance

'''
# To commit & push in pycharm
# 1) VCS>Commit...
# 2) VCS>Git>Push...
'''

def doit(epochs, showFrequency):
    backprop = backProp(2, 10, 2, 0.1)
    #print(backprop.get_weightBottoms())

    rows = len(backprop.get_weightBottoms())
    cols = 0
    if rows:
        cols = len(backprop.get_weightBottoms()[0])
    for j in range(rows):
        for i in range(cols):
                print(str(backprop.get_weightBottoms()[j][i]), "", end="")
        print()

    print()
    rows = len(backprop.get_weightTops())
    cols = 0
    if rows:
        cols = len(backprop.get_weightTops()[0])
    for j in range(rows):
        for i in range(cols):
            print(str(backprop.get_weightTops()[j][i]), "", end="")
        print()

    print()
    for i in backprop.get_biasBottom():
        print(i)
	
    print()
    for i in backprop.get_biasTop():
        print(i)



##############START################

blackjack_print()
doit(1000000, 100000)

