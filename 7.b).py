#Write a program for Hopfield network model for associative memory
import numpy as np

# ---------- Step 1: Define patterns to store ----------
# Patterns: 1D arrays with 1 and -1
patterns = np.array([
    [1, -1, 1, -1],
    [-1, 1, -1, 1],
    [1, 1, -1, -1]
])

num_neurons = patterns.shape[1]

# ---------- Step 2: Create weight matrix using Hebbian learning ----------
W = np.zeros((num_neurons, num_neurons))
for p in patterns:
    W += np.outer(p, p)
np.fill_diagonal(W, 0)  # no self-connection
print("Weight matrix W:\n", W)

# ---------- Step 3: Introduce noisy input ----------
noisy_input = np.array([1, -1, -1, -1])
state = noisy_input.copy()
print("Initial noisy input:", state)

# ---------- Step 4: Update network until convergence ----------
for step in range(10):
    new_state = np.sign(W @ state)
    new_state[new_state == 0] = 1  # treat 0 as +1
    if np.array_equal(new_state, state):
        break
    state = new_state
    print(f"Step {step+1}: {state}")

# ---------- Step 5: Final recovered pattern ----------
print("Recovered pattern:", state)
