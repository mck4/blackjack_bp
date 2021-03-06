'''
backprop.py

the backprop is here
'''


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

    def __init__(self, inputs, hiddens, outputs, eta):
        self.weightBottom = []
        self.weightTop = []
        self.biasBottom = []
        self.biasTop = []
        self.hidden = []
        self.output = []

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
        self.hidden = [0] * self.num_hiddens

        # Fill output with zeros
        self.output = [0] * self.num_outputs


''' FUNCTIONS '''

# Returns a random weight between -1 and 1
def randWeight():
    random_weight = random.uniform(-1.0, 1.0)
    return random_weight

# Returns a prediction
def predictBP(bp, sample):

    # Calculate hidden values
    for k in range(0, bp.num_hiddens):
        sum = 0.0
        for i in range(0, bp.num_inputs):
            sum += bp.weightBottom[i][k] * sample[i]
        sum += bp.biasBottom[k] # Add the bias
        bp.hidden[k] = (1.0 / (1.0 + math.exp(-sum))) # Sigmoid

    # Calculate output values
    for k in range(0, bp.num_outputs):
        sum = 0.0
        for i in range(0, bp.num_hiddens):
            sum += bp.weightTop[i][k] * bp.hidden[i]
        sum += bp.biasTop[k] # Add the bias
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

def adjustWeights(bp, sample, actual):
    sum = None
    # Fill delta with zeros
    delta = [0] * bp.num_outputs

    for k in range(0, bp.num_outputs):
        sum = 1 if (k == actual) else 0 # 1 if correct, otherwise 0
        sum -= bp.output[k]             # predicted

        # Derivative of sigmoid
        delta[k] = sum * bp.output[k] * (1 - bp.output[k])

        # Update weights from hiddens to outputs
        for i in range(0, bp.num_hiddens):
            bp.weightTop[i][k] += bp.eta * delta[k] * bp.hidden[i]

        # Update bias from hiddens to outputs
        bp.biasTop[k] += bp.eta * delta[k]

    for j in range(0, bp.num_hiddens):
        d = 0.0
        for k in range(0, bp.num_outputs):
            d += bp.weightTop[j][k] * delta[k]

        for i in range(0, bp.num_inputs):
            bp.weightBottom[i][j] += bp.eta * bp.hidden[j] * (1 - bp.hidden[j]) * d * sample[i]

        bp.biasBottom[j] += bp.eta * d
