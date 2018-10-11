import start
# This file is empty!
class Card:
    name = None
    value = None
    suit = None
    isDrawn = False

    def __init___(self, suit, name):
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