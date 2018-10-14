# Usual python imports
import random

# Returns a random weight to five decimals places
def randWeight():
    random_weight = round(random.uniform(-1.0, 1.0), 5)
    return random_weight

# backProp class
class backProp:
    num_inputs = None   # Num of Inputs
    num_hiddens = None  # Num of Hiddens
    num_outputs = None  # Num of Outputs
    eta = None
    weightBottoms = []
    weightTops = []
    biasBottom = []
    biasTop = []
    hidden = []
    output = []

    def __init__(self, inputs, hiddens, outputs, eta):
        self.num_inputs = inputs
        self.num_hiddens = hiddens
        self.num_outputs = outputs
        self.eta = eta

        # Select random weights for weightBottoms
        for i in range(self.num_inputs):
            column = []
            for j in range(self.num_hiddens):
                column.append(randWeight())
            self.weightBottoms.append(column)

        # Select random weights for weightTops
        for i in range(self.num_hiddens):
            column = []
            for j in range(self.num_outputs):
                column.append(randWeight())
            self.weightTops.append(column)

        # Select random weights for biasBottom
        for i in range(self.num_hiddens):
            self.biasBottom.append(randWeight())

        # Select random weights for biasTop
        for i in range(self.num_outputs):
            self.biasTop.append(randWeight())

    def get_num_inputs(self):
        return self.num_inputs

    def get_num_hiddens(self):
        return self.num_hiddens

    def get_num_outputs(self):
        return self.num_outputs

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
