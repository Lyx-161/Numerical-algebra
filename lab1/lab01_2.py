import numpy as np
import math

data = [
    4042.045051380452, 0.000531415926535, -2759471.276702747, 0.0000557052996742895,
    2755463.874010974, -34.64291531256604, -0.000031415926535
]

def sequential_sum(data):
    sum=0
    for i in range(len(data)):
        sum+=data[i]
    return sum

def reverse_sum(data):
    l=len(data)
    sum=0
    for i in range(l):
        sum+=data[l-1-i]
    return sum

def cmp(x):
    return abs(x)

def abs_desc_sum(data):
    data.sort(key=cmp,reverse=True)
    sum=0
    for i in range(len(data)):
        sum+=data[i]
    return sum


def abs_asc_sum(data):
    data.sort(key=cmp,reverse=False)
    sum=0
    for i in range(len(data)):
        sum+=data[i]
    return sum

sequential_result = sequential_sum(data)
reverse_result = reverse_sum(data)
abs_desc_result = abs_desc_sum(data)
abs_asc_result = abs_asc_sum(data)

print("Sequential Sum: {:.9e}".format(sequential_result))
print("Reverse Sum: {:.9e}".format(reverse_result))
print("Absolute Descending Sum: {:.9e}".format(abs_desc_result))
print("Absolute Ascending Sum: {:.9e}".format(abs_asc_result))