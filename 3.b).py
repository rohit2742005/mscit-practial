#Write a program to implement of delta rule.
#supervised learning
import numpy as np
x=np.array([1,1,1])
weights=np.array([1,1,1])
desired=np.array([2,3,4])
actual=np.zeros((3,))
a=1
print("Learning Rate : 1")
actual=x*weights
print("actual",actual)
print("desired",desired)
while True:
    if np.array_equal(desired,actual):
        break #no change
    else:
        for i in range(0,3):
            weights[i]=weights[i]+a*(desired[i]-actual[i])
        actual=x*weights
        print("weights",weights)
        print("actual",actual)
        print("desired",desired)
print("*"*30)
print("Final output")
print("Corrected weights",weights)
print("actual",actual)
print("desired",desired)
