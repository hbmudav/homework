from math import inf

def true_divide (first, second):
    if second == 0:
        return inf
    else:
        return first / second
# print(true_divide(4,0))