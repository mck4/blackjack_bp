
# Print the initial state of the network
def print_initial_state(backprop):

    # Getting these values so the code will be way easier to read
    inputs = backprop.get_num_inputs()
    hiddens = backprop.get_num_hiddens()
    outputs = backprop.get_num_outputs()

    print("INITIAL STATE OF NETWORK\n")

    # Show all the input -> hidden weights
    print("weight input (%d) -> hiddens (%d):" % (backprop.get_num_inputs(), backprop.get_num_hiddens()))
    for i in range(0, inputs):
        for j in range(0, hiddens):
            print("%8s " % (str(backprop.get_weightBottoms()[i][j])), end="")
        print()
    print()

    # Show all the hidden -> output weights
    print("weight hiddens (%d) -> outputs (%d):" % (backprop.get_num_inputs(), backprop.get_num_hiddens()))
    for i in range(0, hiddens):
        for j in range(0, outputs):
            print("%8s " % (str(backprop.get_weightTops()[i][j])), end="")
        print()
    print()

    # Show all the hidden biases
    print("Bias for the hiddens: ")
    #prtcount = 1 # go to next line for every five biases
    for i in range(0, hiddens):
        print("%8s " % (str(backprop.get_biasBottom()[i])), end="")
        if ((i+1) % 5) == 0: print()
        #prtcount += 1
    print()

    # Show all the output biases
    print("Bias for the outputs: ")
    for i in range(0, outputs):
        print("%8s " % (str(backprop.get_biasTop()[i])), end="")

    print("")

# Print prediction
def print_prediction():
    pass