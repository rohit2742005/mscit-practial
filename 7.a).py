#Write a program for Linear separation.
import numpy as np
import matplotlib.pyplot as plt

# Function to compute distance and side of a point from line ax + by + c = 0
def create_distance_function(a, b, c):
    def distance(x, y):
        nom = a*x + b*y + c
        if nom == 0:
            pos = 0
        elif (nom<0 and b<0) or (nom>0 and b>0):
            pos = -1
        else:
            pos = 1
        return (np.abs(nom)/np.sqrt(a**2+b**2), pos)
    return distance

# Sample points
points = [(3.5, 1.8), (1.1, 3.9)]

# Plot setup
fig, ax = plt.subplots()
ax.set_xlabel("sweetness")
ax.set_ylabel("sourness")
ax.set_xlim([-1,6])
ax.set_ylim([-1,8])

# Plot points
for i, (x, y) in enumerate(points):
    color = "darkorange" if i==0 else "yellow"
    ax.plot(x, y, "o", color=color, markersize=10)

# X-axis values for lines
X = np.arange(-0.5, 5, 0.1)

# Check slopes from 0 to 1
for x in np.arange(0, 1.05, 0.05):
    slope = np.tan(np.arccos(x))
    dist_func = create_distance_function(slope, -1, 0)
    Y = slope * X
    results = [dist_func(*pt) for pt in points]

    # Plot line green if points on different sides, else red
    if results[0][1] != results[1][1]:
        ax.plot(X, Y, "g-")
    else:
        ax.plot(X, Y, "r-")

plt.show()
