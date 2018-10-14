# Usual python imports
import random

PRINTSIMDETAIL = 1
PRINTSIMDETAILVERBOSE = 1

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

    # GETTERS & SETTERS

    def set_isDrawn(self, value):
        self.isDrawn = value

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

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

    # GETTERS & SETTERS
    def get_deck(self):
        return self.deck

def win_holds(num_playercards, player_total, dealer_total):

    pass

def win_draws(num_playercards, player_total, dealer_total):
    pass

# This simulation will, through, simulations, conclude what the desired output is
def runSimulation(deck, playerC1, playerC2, dealerC1, times):
    hold_wins = 0 # Num of holds resulting in a win
    draw_wins = 0 # Num of draws resulting in a win
    num_playercards = 2 # HARD CODED FOR NOW, could be 3, 4, ... in the future

    # Dealer draws 2nd card which the player can't see
    dealerC2 = deck.get_deck().pop(0) # 48 cards left in the deck

    # Add up the player's card total
    player_total = playerC1.get_value() + playerC2.get_value()
    # Add up the dealer's card total
    dealer_total = dealerC1.get_value() + dealerC2.get_value()

    if(PRINTSIMDETAIL):
        print("PLAYER: %s, %s vs DEALER: %s, (%s)" % (playerC1, playerC2, dealerC1, dealerC2))
        print(len(deck.get_deck()))

    # Run this the given amount of times
    for i in range(0, times):
        # Does holding result in a win?
        if(win_holds(num_playercards, player_total, dealer_total)):
            hold_wins += 1

        # Does drawing result in a win?
        if(win_draws(num_playercards, player_total, dealer_total)):
            draw_wins += 1

    if(draw_wins > hold_wins):
        return 0 # We would want to draw
    else:
        return 1 # We would want to hold