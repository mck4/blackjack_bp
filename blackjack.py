# Usual python imports
import random

PRT = 0
PRTDETAIL = 0

''' CLASSES '''

# Card Class: Represents a single card
class Card:
    name = None     # Name of the card:  Could be '1', 'ace', 'queen', etc
    value = None    # Value of the card: The integer value of a card
    suit = None     # Suit of a card: Not particularly useful but makes the simulation more real?
    isDrawn = False # False if card still in deck; True if drawn

    # To create a card, a suit and a name must be provided; the value is taken from the name
    def __init__(self, suit, name):
        self.name = name
        self.suit = suit

        # Jack, King, & Queen cards all have '10' as an integer value
        if name == "J" or name == "K" or name == "Q":
            self.value = 10
        # Ace can have 1 or 11 but in this case, for ease, it will be just '1'
        elif name == "A":
            self.value = 1
        elif name == "10":
            self.value = 10
            self.name = "T"
        # Else convert the name to an integer value since the above take care of non-int named cards
        else:
            self.value = int(name)

    # String representation of a Card
    def __str__(self):
        cardStr = ("%s of %s" % (self.name, self.suit))
        return cardStr


# Deck Class: represents a deck of 52 Cards
class Deck:
    deck = [] # Empty deck

    # Creating a Deck instance fills the decks with Cards
    def __init__(self):
        # Building the deck from nothing
        empty_deck = []

        # Clubs suit
        for i in range(1, 14):
            suit = "C"
            if i == 1:    card = Card(suit, "A")
            elif i == 11: card = Card(suit, "J")
            elif i == 12: card = Card(suit, "Q")
            elif i == 13: card = Card(suit, "K")
            else:         card = Card(suit, str(i))
            empty_deck.append(card)

        # Diamonds suit
        for i in range(1, 14):
            suit = "D"
            if i == 1:    card = Card(suit, "A")
            elif i == 11: card = Card(suit, "J")
            elif i == 12: card = Card(suit, "Q")
            elif i == 13: card = Card(suit, "K")
            else:         card = Card(suit, str(i))
            empty_deck.append(card)

        # Spades suit
        for i in range(1, 14):
            suit = "S"
            if i == 1:    card = Card(suit, "A")
            elif i == 11: card = Card(suit, "J")
            elif i == 12: card = Card(suit, "Q")
            elif i == 13: card = Card(suit, "K")
            else:         card = Card(suit, str(i))
            empty_deck.append(card)

        # Hearts suit
        for i in range(1, 14):
            suit = "H"
            if i == 1:    card = Card(suit, "A")
            elif i == 11: card = Card(suit, "J")
            elif i == 12: card = Card(suit, "Q")
            elif i == 13: card = Card(suit, "K")
            else:         card = Card(suit, str(i))
            empty_deck.append(card)

        # Set newly created as the object's new deck
        self.deck = empty_deck

    # String representation of a Deck
    def __str__(self):
        # For every 13 cards, separate by a newline
        counttemp = 0

        # Heading
        deckStr = ""
        deckStr += "Current state of Deck \n"

        # Print each card
        for i in self.deck:
            if (counttemp % 13) == 0:
                deckStr += "\n"
            deckStr += str(i) + "\n"
            counttemp += 1

        return deckStr

    # Shuffles deck
    def shuffle_deck(self):
        return random.shuffle(self.deck)


''' FUNCTIONS '''

# If we decide to hold -> 1 denotes a win; 0 denotes a loss
def win_holds(deck, num_playercards, player_total, dealer_total, curindex):

    # Instead of popping cards which alters the deck, the dealer will
    # draw from the top and advance to the next card in the deck
    # Keep track of index
    index = curindex


    # Five Card Charlie
    #if (num_playercards >= 5):
    #    # Player wins if the five cards are less than 20
    #    if (player_total <= 21):
    #        # player wins
    #        if (PRTDETAIL): print(" P(%d), D(%d) -> P: Wins" % (player_total, dealer_total), end="")
    #        if (PRT): print(" P wins; 5 card charlie")
    #        return 1


    while(1):
        if((PRTDETAIL or PRT) and index == 0): print("\n  HOLD -> ", end="")
        # Dealer busts - Total greater then 21
        if dealer_total > 21:
            if(PRTDETAIL): print(" P(%d), D(%d) -> D: Bust" % (player_total, dealer_total), end="")
            if (PRT): print(" P wins", end="")
            return 1

        # Dealer's Current hand is acceptable - total greater than 16
        if(dealer_total > 16):
            # Dealer Wins - Tie or the dealer's total is greater than players
            if(dealer_total >= player_total):
                if (PRTDETAIL): print(" P(%d), D(%d) -> D: Win" % (player_total, dealer_total), end="")
                if (PRT): print(" P loses", end="")
                return 0
            # Player Wins - Total greater than dealer's
            else:
                if (PRTDETAIL): print(" P(%d), D(%d) -> P: Win" % (player_total, dealer_total), end="")
                if (PRT): print(" P wins", end="")
                return 1
        # Dealer's Current hand is unacceptable - must draw another card
        else:
            # Dealer draws a card
            dealer_drawNewCard = deck.deck[index]

            if (PRTDETAIL): print(" %s, " % dealer_drawNewCard, end="")

            index += 1 # Increment index
            # Add to dealer total
            dealer_total += dealer_drawNewCard.value

# If we decide to draw -> 1 denotes a win; 0 denotes a loss
def win_draws(deck, num_playercards, player_total, dealer_total, curindex):

    # Instead of popping cards which alters the deck, the dealer will
    # draw from the top and advance to the next card in the deck
    # Keep track of index
    index = curindex

    # Player draws a card
    player_drawNewCard = deck.deck[index]
    # Add to player total
    player_total += player_drawNewCard.value
    num_playercards += 1  # Increment player's cards

    # Five Card Charlie
    if (num_playercards >= 5):
        # Player wins if the five cards are less than 20
        if (player_total <= 21):
            # player wins
            if (PRTDETAIL): print(" P(%d), D(%d) -> P: Wins" % (player_total, dealer_total), end="")
            if (PRT): print(" P wins; 5 card charlie", end="")
            return 1

    index += 1 # Increment index

    if (PRTDETAIL or PRT):
        if(index == 1): print("\n  DRAW -> ", end="")
        else: print(" DRAW -> ", end="")
    if (PRTDETAIL): print(" %s, " % player_drawNewCard, end="")

    # If the player busts after a draw
    if(player_total > 21):
        if (PRTDETAIL): print(" P(%d), D(%d) -> P: Bust" % (player_total, dealer_total), end="")
        if (PRT): print(" P loses", end="")
        return 0

    # If the player total is greater than 16
    # I guess this an arbitrary number sorta though it makes sense; it is a sim after all
    if(player_total > 16):
        # Hold since we have a high number
        if(win_holds(deck, num_playercards, player_total, dealer_total, index)):
            return 1
    else:
        # Draw since we have a low number
        if (win_draws(deck, num_playercards, player_total, dealer_total, index)):
            return 1

    # Probably for the recursive call
    return 0


''' RUN SIMULATION '''

# This simulation will conclude what the desired output is
def runSimulation(deck, playerC1, playerC2, dealerC1, times, i):

    if( i == 11 ):
        global PRT
        PRT = 0
        global PRTDETAIL
        PRTDETAIL = 0


    hold_wins = 0 # Num of holds resulting in a win
    draw_wins = 0 # Num of draws resulting in a win
    num_playercards = 2 # HARD CODED FOR NOW, could be 3, 4, ... in the future

    # Dealer draws 2nd card which the player can't see
    dealerC2 = deck.deck.pop(0) # 48 cards left in the deck

    # Add up the player's card total
    player_total = playerC1.value + playerC2.value
    # Add up the dealer's card total
    dealer_total = dealerC1.value + dealerC2.value

    if(PRT or PRTDETAIL):
        print("P(%d): %s, %s vs. D(%d): %s, [%s] " %
              (player_total, playerC1, playerC2, dealer_total, dealerC1, dealerC2), end="")

    # Run this the given amount of times
    for i in range(0, times):
        #print("%d) " % (i + 1))

        # Shuffle deck
        deck.shuffle_deck()

        # Does holding result in a win?
        if(win_holds(deck, num_playercards, player_total, dealer_total, 0)):
            hold_wins += 1

        # Does drawing result in a win?
        if(win_draws(deck, num_playercards, player_total, dealer_total, 0)):
            draw_wins += 1


    if (PRT or PRTDETAIL):
        print("\nDraw wins: %d, Hold wins: %d" % (draw_wins, hold_wins))

    # Do we draw or do we hold?
    if(draw_wins > hold_wins): return 0 # Draw
    else: return 1                      # Hold

def runSimulation2(deck, playerC1, playerC2, playerC3, dealerC1, times, i):

    if( i == 11 ):
        global PRT
        PRT = 0
        global PRTDETAIL
        PRTDETAIL = 0


    hold_wins = 0 # Num of holds resulting in a win
    draw_wins = 0 # Num of draws resulting in a win
    num_playercards = 3

    # Dealer draws 2nd card which the player can't see
    dealerC2 = deck.deck.pop(0) # 48 cards left in the deck

    # Add up the player's card total
    player_total = playerC1.value + playerC2.value + playerC3.value
    # Add up the dealer's card total
    dealer_total = dealerC1.value + dealerC2.value

    if(PRT or PRTDETAIL):
        print("P(%d): %s, %s vs. D(%d): %s, [%s] " %
              (player_total, playerC1, playerC2, dealer_total, dealerC1, dealerC2), end="")

    # Run this the given amount of times
    for i in range(0, times):
        #print("%d) " % (i + 1))

        # Shuffle deck
        deck.shuffle_deck()

        # Does holding result in a win?
        if(win_holds(deck, num_playercards, player_total, dealer_total, 0)):
            hold_wins += 1

        # Does drawing result in a win?
        if(win_draws(deck, num_playercards, player_total, dealer_total, 0)):
            draw_wins += 1


    if (PRT or PRTDETAIL):
        print("\nDraw wins: %d, Hold wins: %d" % (draw_wins, hold_wins))

    # Do we draw or do we hold?
    if(draw_wins > hold_wins): return 0 # Draw
    else: return 1                      # Hold
