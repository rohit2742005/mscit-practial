#Write a program for Radial Basis function
import numpy as np
from scipy.linalg import pinv
import matplotlib.pyplot as plt

# ---------- Input and Target ----------
x = np.linspace(-1, 1, 50).reshape(-1, 1)  # 1D input
y = np.sin(3*(x + 0.5)**3 - 1)            # target function

# ---------- RBF Parameters ----------
numCenters = 5
sigma = 0.3

# ---------- Choose Centers ----------
centers = x[np.linspace(0, len(x)-1, numCenters, dtype=int)]

# ---------- Gaussian RBF Function ----------
def rbf(xi, c, sigma):
    return np.exp(-np.linalg.norm(xi - c)**2 / (2*sigma**2))

# ---------- Activation Matrix ----------
G = np.zeros((len(x), numCenters))
for i, xi in enumerate(x):
    for j, c in enumerate(centers):
        G[i, j] = rbf(xi, c, sigma)

# ---------- Compute Output Weights ----------
W = np.dot(pinv(G), y)

# ---------- Compute Network Output ----------
y_pred = np.dot(G, W)

# ---------- Plot ----------
plt.plot(x, y, 'k-', label='Original function')
plt.plot(x, y_pred, 'r-', label='RBF output', linewidth=2)
plt.plot(centers, np.zeros(numCenters), 'gs', label='RBF centers')
plt.legend()
plt.show()
