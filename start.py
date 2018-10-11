#import blackjack
# Can you see this?
# I was thinking maybe it would be ideal to separate the bp, the main(start.py),
# and blackjack.py for the simulator, you know, like Dr. O'Hara did it. I don't think
# Python gives you too difficult of a time doing that.

# I'm not sure if we would need two bps for the two and three # card hand?
# I don't think so but I didn't make it yet for this reason.
# By the way if you want to make separate .py files for the classes, feel free.

#If you want it to show up on github, make sure you commit and push. I was just committing &
#it wasn't showing up but when I pushed, it showed up

# So, in order:
# 1) VCS>Commit...
# 2) VCS>Git>Push...

#TEST

import random

# Returns a random weight to five decimals places
def randWeight():
    random_weight = round(random.uniform(-1.0, 1.0), 5)
    return random_weight

class backProp:
    inputs = None
    hiddens = None
    outputs = None
    eta = None
    weightBottoms = []
    weightTops = []
    biasBottom = []
    biasTop = []
    hidden = []
    output = []

    def __init__(self, inputs, hiddens, outputs, eta):
        self.inputs = inputs
        self.hiddens = hiddens
        self.outputs = outputs
        self.eta = eta

        for i in range(self.inputs):
            column = []
            for j in range(self.hiddens):
                column.append(randWeight())
            self.weightBottoms.append(column)


        for i in range(self.hiddens):
            column = []
            for j in range(self.outputs):
                column.append(randWeight())
            self.weightTops.append(column)

        for i in range(self.hiddens):
            self.biasBottom.append(randWeight())

        for i in range(self.outputs):
            self.biasTop.append(randWeight())

    def get_inputs(self):
        return self.inputs

    def get_hiddens(self):
        return self.hiddens

    def get_outputs(self):
        return self.outputs

    def get_eta(self):
        return self.eta

    def get_weightBottoms(self):
        return self.weightBottoms

    def get_weightTops(self):
        return self.weightTops

    def get_biasBottom(self):
        return self.biasBottom

    def get_biasTop(self):
        return self.biasTop

    def get_hidden(self):
        return self.hidden

    def get_output(self):
        return self.output

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

doit(1000000, 100000)
#print(randWeight())