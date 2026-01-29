#Write a program to implement Hebb’s rule.
import numpy as np
x1=np.array([1,1,1,-1,1,-1,1,1,1])
x2=np.array([1,1,1,1,-1,1,1,1,1])
b=0
y=np.array([1,-1])
wtnew=np.zeros((9,))
print("First input with target =1")
for i in range(0,9):
    wtnew[i]=wtnew[i]+x1[i]*y[0]
b=b+y[0]
print("new wt =", wtnew)
print("Bias value",b)
print("Second input with target =-1")
for i in range(0,9):
    wtnew[i]=wtnew[i]+x2[i]*y[1]
b=b+y[1]
print("new wt =", wtnew)
print("Bias value",b)
