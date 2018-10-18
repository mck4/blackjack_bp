'''
print.py

prints details about the backprop
'''

# Print the initial state of the network
def print_initial_state(backprop):

    # Show all the input -> hidden weights
    print("weight input (%d) -> hiddens (%d):" % (backprop.num_inputs, backprop.num_hiddens))
    for i in range(0, backprop.num_inputs):
        for j in range(0, backprop.num_hiddens):
            print("%8.5f " % (backprop.weightBottom[i][j]), end="")
        print()
    print()

    # Show all the hidden -> output weights
    print("weight hiddens (%d) -> outputs (%d):" % (backprop.num_inputs, backprop.num_hiddens))
    for i in range(0, backprop.num_hiddens):
        for j in range(0, backprop.num_outputs):
            print("%8.5f " % (backprop.weightTop[i][j]), end="")
        print()
    print()

    # Show all the hidden biases
    print("Bias for the hiddens: ")
    for i in range(0, backprop.num_hiddens):
        print("%8.5f " % (backprop.biasBottom[i]), end="")
        if ((i+1) % 5) == 0: print()
    print()

    # Show all the output biases
    print("Bias for the outputs: ")
    for i in range(0, backprop.num_outputs):
        print("%8.5f " % (backprop.biasTop[i]), end="")

    print("")

# Print prediction
def print_prediction(backprop, sample):
    for k in range(0, backprop.num_hiddens):
        print("Hidden [%d] = sigmoid (" % k, end="")
        for i in range(0, backprop.num_inputs):
            if i > 0: print(" + ", end="")
            print("%3.1f * %6.3f" % (sample[i], backprop.weightBottom[i][k]), end="")
        print(" + %6.3f" %backprop.biasBottom[k], end = "")
        print(") = %6.3f" %backprop.hidden[k])
    print()

    for k in range (0, backprop.num_outputs):
        print("Output[%d] = sigmoid(" %k, end="")
        for i in range (0, backprop.num_hiddens):
            if i>0 : print(" +" , end="")
            print("%6.3f * %6.3f" %(backprop.hidden[i], backprop.weightTop[i][k]), end="")
        print("+ %6.3f" %backprop.biasTop[k], end="")
        print(") = %6.3f" %backprop.output[k])
