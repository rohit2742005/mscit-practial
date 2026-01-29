#Write a program for error Backpropagation algorithm.
import math

# Input and target
a0 = -1
t = -1

# Given values (no input)
w10 = 12
b10 = 35
w20 = 23
b20 = 45
c   = 11

# ---------- Forward Pass ----------
n1 = w10*a0 + b10
a1 = math.tanh(n1)

n2 = w20*a1 + b20
a2 = math.tanh(n2)

# ---------- Error Calculation ----------
e = t - a2

# ---------- Backward Pass ----------
s2 = -2 * (1 - a2*a2) * e
s1 = (1 - a1*a1) * w20 * s2

# ---------- Weight and Bias Update ----------
w11 = w10 - c * s1 * a0
w21 = w20 - c * s2 * a1
b11 = b10 - c * s1
b21 = b20 - c * s2

# ---------- Output ----------
print("Updated weight of first network w11 =", w11)
print("Updated weight of second network w21 =", w21)
print("Updated bias of first network b11 =", b11)
print("Updated bias of second network b21 =", b21)
