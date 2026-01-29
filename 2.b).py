#Generate XOR function using McCulloch-Pitts neural net.
# Simple McCulloch–Pitts XOR
for A in [0, 1]:
    for B in [0, 1]:
        # Hidden layer
        if (A + B) >= 1: # OR neuron
            H1 = 1
        else:
            H1 = 0
        if (A + B) >= 2: # AND neuron
            H2 = 1
        else:
            H2 = 0
        # Output neuron
        if (H1 - 2 * H2) >= 1:
            O = 1
        else:
            O = 0
        print(f"A={A}, B={B} -> XOR={O}")
