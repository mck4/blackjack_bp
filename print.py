
# Print the initial state of the network
def print_initial_state(backprop):

    print("INITIAL STATE OF NETWORK\n")

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
def print_prediction():
    pass