# important   to importing nampy library
import numpy as np

def StepFunction(threshold):
if threshold >= 3.1:
return 1
else:
return 0
# designing the Perceptron
def designed_Percept(x, weight, bias):
threshold = np.dot(weight, x) + bias
# print("Thereshold: ", threshold)
y = StepFunction(threshold)
return y

# w1 = 0.9, w2 = 0.8, bias = 0.7
def OR_logic(x):
weight = np.array([0.9, 0.8])
bias =0.7
return designed_Perceptron(x, weight, bias)
#  Perceptron Model
input_01 = np.array([0, 1])
input_11 = np.array([1, 1])
input_00 = np.array([0, 0])
input_10 = np.array([1, 0])
print("OR({}, {}) = {}".format(0, 0, OR_logic(input_00)))
print("OR({}, {}) = {}".format(0, 1, OR_logic(input_01)))
print("OR({}, {}) = {}".format(1, 0, OR_logic(input_10)))print("OR({}, {}) = {}".format(1, 1, OR_logic(input_11)))

