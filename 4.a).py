#Write a program for Back Propagation Algorithm
import numpy as np
import math

# Given values
v1 = np.array([0.6, 0.3])
v2 = np.array([-0.1, 0.4])
w  = np.array([-0.2, 0.4, 0.1])
b1, b2 = 0.3, 0.5
x1, x2 = 0, 1
alpha = 0.25

# Forward pass
zin1 = b1 + x1*v1[0] + x2*v2[0]
zin2 = b2 + x1*v1[1] + x2*v2[1]

z1 = 1/(1+math.exp(-zin1))
z2 = 1/(1+math.exp(-zin2))

yin = w[0] + z1*w[1] + z2*w[2]
y = 1/(1+math.exp(-yin))

# Backward pass
dk = (1-y)*y*(1-y)

dw1 = alpha * dk * z1
dw2 = alpha * dk * z2
dw0 = alpha * dk

d1 = dk*w[1] * z1*(1-z1)
d2 = dk*w[2] * z2*(1-z2)

# Weight updates
v1 += [alpha*d1*x1, alpha*d2*x1]
v2 += [alpha*d1*x2, alpha*d2*x2]
b1 += alpha*d1
b2 += alpha*d2

w[0] += dw0
w[1] += dw1
w[2] += dw2

np.set_printoptions(precision=2)
print("Updated weights:", v1, v2, w)
print("Updated bias:", round(b1,2), round(b2,2))