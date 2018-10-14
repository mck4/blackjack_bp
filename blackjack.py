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

    # GETTERS & SETTERS
    def get_deck(self):
        return self.deck

def win_holds(deck, num_playercards, player_total, dealer_total):
    # 1 denotes a win; 0 denotes a loss

    # Instead of popping cards, the dealer will draw from the top and advance to the next card in the deck
    # Keep track of the index
    index = 0

    # Five Card Charlie
    if(num_playercards >= 5): return 1

    while(1):
        if(PRINTSIMDETAILVERBOSE and index == 0): print("HOLD -> ", end="")
        # Dealer busts - Total greater then 21
        if dealer_total > 21:
            if(PRINTSIMDETAILVERBOSE): print(" P(%d), D(%d) -> D: Bust" % (player_total, dealer_total))
            return 1

        # Dealer's Current hand is acceptable - total greater than 16
        if(dealer_total > 16):
            # Dealer Wins - Tie or the dealer's total is greater than players
            if(dealer_total >= player_total):
                if (PRINTSIMDETAILVERBOSE): print(" P(%d), D(%d) -> D: Win" % (player_total, dealer_total))
                return 0
            # Player Wins - Total greater than dealer's
            else:
                if (PRINTSIMDETAILVERBOSE): print(" P(%d), D(%d) -> P: Win" % (player_total, dealer_total))
                return 1
        # Dealer's Current hand is unacceptable - must draw another card
        else:
            drawNewCard = deck.get_deck()[index]
            print(" %s, " % drawNewCard, end="")
            index += 1
            dealer_total += drawNewCard.get_value()


def win_draws(deck, num_playercards, player_total, dealer_total):
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
        print("P(%d): %s, %s vs. D(%d): %s, [%s] " %
              (player_total, playerC1, playerC2, dealer_total, dealerC1, dealerC2))
        #print(len(deck.get_deck()))

    # Run this the given amount of times
    for i in range(0, times):
        print("%d) " % (i + 1), end="")

        # Shuffle deck
        deck.shuffle_deck()

        # Does holding result in a win?
        if(win_holds(deck, num_playercards, player_total, dealer_total)):
            hold_wins += 1

        # Does drawing result in a win?
        #if(win_draws(deck, num_playercards, player_total, dealer_total)):
         #   draw_wins += 1
    #print()

    if(draw_wins > hold_wins): return 0 # We would want to draw
    else: return 1 # We would want to hold