#Kohonen Self organizing map
from minisom import MiniSom
import matplotlib.pyplot as plt

# ---------- Input Data ----------
data = [
    [0.80, 0.55, 0.22, 0.03],
    [0.82, 0.50, 0.23, 0.03],
    [0.80, 0.54, 0.22, 0.03],
    [0.80, 0.53, 0.26, 0.03],
    [0.79, 0.56, 0.22, 0.03],
    [0.75, 0.60, 0.25, 0.03],
    [0.77, 0.59, 0.22, 0.03]
]

# ---------- Initialize SOM ----------
# 6x6 grid, input dimension 4, sigma=0.3, learning_rate=0.5
som = MiniSom(x=6, y=6, input_len=4, sigma=0.3, learning_rate=0.5)

# ---------- Train SOM ----------
som.train_random(data, num_iteration=100)

# ---------- Visualize SOM ----------
plt.imshow(som.distance_map())  # distance map (U-matrix)
plt.title("SOM Distance Map")
plt.colorbar()
plt.show()
