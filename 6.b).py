#Adaptive resonance theory
import numpy as np

# ---------- Input Patterns ----------
X = np.array([
    [1,0,1,0],
    [1,1,0,0],
    [0,0,1,1],
    [0,1,1,0]
])

# ---------- Parameters ----------
num_features = X.shape[1]
num_categories = 5          # max categories
rho = 0.7                   # vigilance
W = np.ones((num_categories, num_features))  # initial weights

# ---------- Training ART 1 ----------
for x in X:
    match_found = False
    for j in range(num_categories):
        # Compute match (dot product / sum of input)
        match = np.dot(x, W[j]) / np.sum(x)
        if match >= rho:
            # Resonance: update weights
            W[j] = W[j] * x
            match_found = True
            print(f"Pattern {x} assigned to category {j+1}")
            break
    if not match_found:
        print(f"Pattern {x} creates new category")

# ---------- Display Final Weight Matrix ----------
print("\nFinal category weights:")
print(W)
