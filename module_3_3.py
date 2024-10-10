def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(b = 25)
print_params(c = [1, 2, 3])
value_list = [2, [321], 'str']
value_dict = {'a':4, 'b':5, 'c':6}
print_params(*value_list)
print_params(**value_dict)
value_list2 = [8.7, 'oka']
print_params(*value_list2, 42)