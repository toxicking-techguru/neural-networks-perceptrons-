import numpy as np

def StepFunction(threshold):
if threshold >= -1.5:
return 1
else:
return 0

def perceptMod(x, weight, b):
threshold = np.dot(weight, x) + b
# print("Thereshold: ", threshold)
y = StepFunction(threshold)
return y
# NOT Logic Function
# weight_NOT = -1, bias_NOT = 0.5
def NOT_Funtion(x):
weight_NOT = -1
bias_NOT = 0.5return perceptMod (x, weight_NOT, bias_NOT)

#  given w1 = 0.9, w2 = 0.8, bias_OR = 0.7
def OR_Function(x):
weight = np.array([0.9, 0.8])
bias_OR = 0.7
return perceptMod(x, weight, bias_OR)
# NOR Logic Function with OR and NOT


def NOR_Functon(x):
OR_out = OR_Function(x)
NOT_output = NOT_Function(OR_out)
return NOT_output
# test
input_01 = np.array([0, 1])
input_11 = np.array([1, 1])
input_00 = np.array([0, 0])
input_10 = np.array([1, 0])
print("NOR({}, {}) = {}".format(0, 0, NOR_Function(input_00)))
print("NOR({}, {}) = {}".format(0, 1, NOR_Function(input_01)))
print("NOR({}, {}) = {}".format(1, 0, NOR_Function(input_10)))
print("NOR({}, {}) = {}".format(1, 1, NOR_Function(input_11)))


