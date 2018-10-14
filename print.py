
def print_initial_state(backprop):
    print("INITIAL STATE OF NETWORK\n")

    print("weight input (%d) -> hiddens (%d)" % (backprop.get_num_inputs(), backprop.get_num_hiddens()))
    rows = len(backprop.get_weightBottoms())
    cols = 0
    if rows:
        cols = len(backprop.get_weightBottoms()[0])
    for j in range(rows):
        for i in range(cols):
                print("%8s " % (str(backprop.get_weightBottoms()[j][i])), end="")
        print()

    print()
    print("weight hiddens (%d) -> outputs (%d)" % (backprop.get_num_inputs(), backprop.get_num_hiddens()))

    rows = len(backprop.get_weightTops())
    cols = 0
    if rows:
        cols = len(backprop.get_weightTops()[0])
    for j in range(rows):
        for i in range(cols):
            print("%8s " % (str(backprop.get_weightTops()[j][i])), end="")
        print()

    print()
    print("Bias for the hiddens ", end="")
    count = 1
    for i in backprop.get_biasBottom():
        print("%8s " % (str(i)), end="")
        if (count % 5) == 0:
            print()
        count += 1

    print("")

    print("Bias for the outputs ", end="")
    for i in backprop.get_biasTop():
        print("%8s " % (str(i)), end="")

    print("")