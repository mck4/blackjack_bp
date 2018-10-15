# Usual python imports
import random
import math

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
        for i in range(0, self.num_inputs):
            column = []
            for j in range(self.num_hiddens):
                column.append(randWeight())
            self.weightBottom.append(column)

        # Select random weights for weightTops
        for i in range(0, self.num_hiddens):
            column = []
            for j in range(self.num_outputs):
                column.append(randWeight())
            self.weightTop.append(column)

        # Select random weights for biasBottom
        for i in range(0, self.num_hiddens):
            self.biasBottom.append(randWeight())

        # Select random weights for biasTop
        for i in range(0, self.num_outputs):
            self.biasTop.append(randWeight())

        # Fill hidden with zeros
        for i in range(0, self.num_hiddens):
            self.hidden.append(0)

        # Fill output with zeros
        for i in range(0, self.num_outputs):
            self.output.append(0)


''' FUNCTIONS '''

# Returns a random weight to five decimals places
def randWeight():
    random_weight = round(random.uniform(-1.0, 1.0), 5)
    return random_weight

def predictBP(bp, sample):

    # Calculate hidden values
    for k in range(0, bp.num_hiddens):
        sum = 0.0
        for i in range(0, bp.num_inputs):
            sum += bp.weightBottom[i][k] * sample[i]
        sum += bp.biasBottom[k]
        bp.hidden[k] = (1.0 / (1.0 + math.exp(-sum))) # Sigmoid


    # Calculate output values
    for k in range(0, bp.num_outputs):
        sum = 0.0
        for i in range(0, bp.num_hiddens):
            sum += bp.weightTop[i][k] * bp.hidden[i]
        sum += bp.biasTop[k]
        bp.output[k] = 1.0 / (1.0 + math.exp(-sum)) # Sigmoid

    i = 0
    # Find highest output activation (output = i)
    for k in range(0, bp.num_outputs):
        if(bp.output[k] > bp.output[i]):
            i = k

    # Find second largest number
    nextMaxSum = -1.0
    for k in range(0, bp.num_outputs):
        if (k != i):
            if(nextMaxSum < 0.0 or bp.output[k] > nextMaxSum):
                nextMaxSum = bp.output[k]

    confidence = bp.output[i] - nextMaxSum

    return (i, confidence)

def adjustWeights():
    pass