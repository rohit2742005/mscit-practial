#Write a program for Hopfield Network.
import numpy as np

# ---------- Stored Patterns (Bipolar: +1, -1) ----------
p1 = np.array([1, -1, 1, -1])
p2 = np.array([-1, 1, -1, 1])

# ---------- Initialize Weight Matrix ----------
W = np.zeros((4, 4))

# Hebbian Learning Rule: W = sum(p * p^T)
W += np.outer(p1, p1)
W += np.outer(p2, p2)
np.fill_diagonal(W, 0)  # No self-connections

print("Weight Matrix:\n", W)

# ---------- Test Pattern ----------
x = np.array([1, -1, 1, -1])

# ---------- Recall Phase ----------
y = np.sign(np.dot(W, x))  # Hopfield update
print("Output Pattern:", y)
