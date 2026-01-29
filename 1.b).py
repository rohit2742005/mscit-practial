#Calculate the output of neural net using both binary and bipolar sigmoidal function.
print("the inputs")
inputs = [0.3,0.5,0.6]
print(inputs)
print("the weights")
weights = [0.2,0.1,-0.3]
print(weights)
print("The net input can be calculated as Yin = x1w1 + x2w2 + x3w3")
Yin = []
for i in range(0, 3):
    Yin.append(inputs[i]*weights[i])
print(round(sum(Yin),3))
