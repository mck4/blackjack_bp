# Usual python imports
import random

# Returns a random weight to five decimals places
def randWeight():
    random_weight = round(random.uniform(-1.0, 1.0), 5)
    return random_weight

# backProp class
class backProp:
    inputs = None   # Inputs
    hiddens = None  # Hiddens
    outputs = None  # Outputs
    eta = None      # A variable for
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
