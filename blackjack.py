#import start
# This file is empty!
class Card:
    name = None
    value = None
    suit = None
    isDrawn = False

    def __init__(self, suit, name):
        self.name = name
        self.suit = suit

        if name == "jack" or name == "king" or name == "queen":
            self.value = 10
        elif name == "ace":
            self.value = 1
        else:
            self.value = int(name)

    def setisDrawn(self, value):
        self.isDrawn = value

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getSuit(self):
        return self.suit

    def __str__(self):
        cardStr = ""
        cardStr += self.suit + " "
        cardStr += self.name
        cardStr += "\n"
        return cardStr

class Deck:
    deck = []

    def __init__(self):
        for i in range(1, 14):
            suit = "clubs"

            if i == 1:    card = Card(suit, "ace")
            elif i == 11: card = Card(suit, "jack")
            elif i == 12: card = Card(suit, "queen")
            elif i == 13: card = Card(suit, "king")
            else:         card = Card(suit, str(i))

            self.deck.append(card)

        for i in range(1, 14):
            suit = "diamonds"

            if i == 1:    card = Card(suit, "ace")
            elif i == 11: card = Card(suit, "jack")
            elif i == 12: card = Card(suit, "queen")
            elif i == 13: card = Card(suit, "king")
            else:         card = Card(suit, str(i))

            self.deck.append(card)

        for i in range(1, 14):
            suit = "spades"

            if i == 1:    card = Card(suit, "ace")
            elif i == 11: card = Card(suit, "jack")
            elif i == 12: card = Card(suit, "queen")
            elif i == 13: card = Card(suit, "king")
            else:         card = Card(suit, str(i))

            self.deck.append(card)

        for i in range(1, 14):
            suit = "hearts"

            if i == 1:    card = Card(suit, "ace")
            elif i == 11: card = Card(suit, "jack")
            elif i == 12: card = Card(suit, "queen")
            elif i == 13: card = Card(suit, "king")
            else:         card = Card(suit, str(i))

            self.deck.append(card)

    def __str__(self):
        restr = ""
        restr += "black jack deck \n"
        for i in self.deck:
            restr+= str(i)
        return restr

    def getdeck(self):
        return self.deck

deck = Deck()
print(deck)
print(len(deck.getdeck()))

