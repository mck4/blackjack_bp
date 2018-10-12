# Usual python imports
import random

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
        if name == "jack" or name == "king" or name == "queen":
            self.value = 10
        # Ace can have 1 or 11 but in this case, for ease, it will be just '1'
        elif name == "ace":
            self.value = 1
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
        cardStr = ("%s of %s: %s" % (self.name, self.suit, str(self.value)))
        return cardStr
'''
    # attempt to condense printing of cards but will fix later
    def printCard_small(self):
        print("%c of %s: %s\n" % (self.name, self.suit, str(self.value)))
'''

# Deck Class: represents a deck of 52 Cards
class Deck:
    deck = [] # Empty deck

    # Creating a Deck instance fills the decks with Cards
    def __init__(self):

        # Clubs suit
        for i in range(1, 14):
            suit = "clubs"
            if i == 1:    card = Card(suit, "ace")
            elif i == 11: card = Card(suit, "jack")
            elif i == 12: card = Card(suit, "queen")
            elif i == 13: card = Card(suit, "king")
            else:         card = Card(suit, str(i))
            self.deck.append(card)

        # Diamonds suit
        for i in range(1, 14):
            suit = "diamonds"
            if i == 1:    card = Card(suit, "ace")
            elif i == 11: card = Card(suit, "jack")
            elif i == 12: card = Card(suit, "queen")
            elif i == 13: card = Card(suit, "king")
            else:         card = Card(suit, str(i))
            self.deck.append(card)

        # Spades suit
        for i in range(1, 14):
            suit = "spades"
            if i == 1:    card = Card(suit, "ace")
            elif i == 11: card = Card(suit, "jack")
            elif i == 12: card = Card(suit, "queen")
            elif i == 13: card = Card(suit, "king")
            else:         card = Card(suit, str(i))
            self.deck.append(card)

        # Hearts suit
        for i in range(1, 14):
            suit = "hearts"
            if i == 1:    card = Card(suit, "ace")
            elif i == 11: card = Card(suit, "jack")
            elif i == 12: card = Card(suit, "queen")
            elif i == 13: card = Card(suit, "king")
            else:         card = Card(suit, str(i))
            self.deck.append(card)

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

    def shuffle_deck(self):
        return random.shuffle(self.deck)

    # GETTERS & SETTERS
    def get_deck(self):
        return self.deck
'''
    # Attempt to print a more condensed version of card but will mess with later
    def printdeck_small(self):
        counttemp = 0
        for i in self.deck:
            if(counttemp % 5) == 0:
                print("")
'''


'''
Possible issues:
Are we using the same deck for each simulation?
Meaning, the cards will deplete over time until we run out.

OR, are we resetting the deck (putting the cards back) for each win/loss?
This makes more sense to me. 
What this means though is that we'll have to 
'''

def blackjack_print():
    deck = Deck()
    print(deck)
    deck.shuffle_deck()

    shuffledDeck = deck.get_deck()

    print("Five random cards")
    for i in range(0, 5):
        print("%d) %s; Size of deck: %d " % (i + 1, shuffledDeck.pop(), len(shuffledDeck)))

    print("")

    #print(decktemp[1])
    #print(deck.get_deck()[1].get_name())
    #print("%c" % (deck.get_deck()[0].get_name()[0]))

