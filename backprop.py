# Usual python imports
import random

''' CLASSES '''
# backProp class
class backProp:
    num_inputs = None   # Num of Inputs
    num_hiddens = None  # Num of Hiddens
    num_outputs = None  # Num of Outputs
    eta = None
    weightBottom = []
    weightTop = []
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
            self.weightBottom.append(column)

        # Select random weights for weightTops
        for i in range(self.num_hiddens):
            column = []
            for j in range(self.num_outputs):
                column.append(randWeight())
            self.weightTop.append(column)

        # Select random weights for biasBottom
        for i in range(self.num_hiddens):
            self.biasBottom.append(randWeight())

        # Select random weights for biasTop
        for i in range(self.num_outputs):
            self.biasTop.append(randWeight())

    # GETTERS & SETTERS

    '''
    def get_num_inputs(self):
        return self.num_inputs

    def get_num_hiddens(self):
        return self.num_hiddens

    def get_num_outputs(self):
        return self.num_outputs

    def get_eta(self):
        return self.eta

    
    def get_weightBottom(self):
        return self.weightBottom

    def get_weightTop(self):
        return self.weightTop

    def get_biasBottom(self):
        return self.biasBottom

    def get_biasTop(self):
        return self.biasTop

    def get_hidden(self):
        return self.hidden

    def get_output(self):
        return self.output

    def set_hidden(self, value):
        self.hidden = value

    def set_output(self, value):
        self.output = value

    def set_weightBottom(self, value):
        self.weightBottom = value

    def set_weightTop(self, value):
        self.weightTop = value

    def set_biasBottom(self, value):
        self.biasBottom = value

    def set_biasTop(self, value):
        self.biasTop = value
    '''
''' FUNCTIONS '''

# Returns a random weight to five decimals places
def randWeight():
    random_weight = round(random.uniform(-1.0, 1.0), 5)
    return random_weight

def predictBP(backprop, sample, confidence):

    # Calculate hidden values
    for k in range(0, backprop.num_hiddens):
        sum = 0.0
        for i in range(0, backprop.num_inputs):
            sum += backprop.weightBottom[i][k] * sample[i]
        sum += backprop.biasBottom[k]

def adjustWeights():
    pass