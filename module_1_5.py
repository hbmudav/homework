immutable_var = 1, 3, 5, True, 'Alexandr', [2, 4, 6]
print(immutable_var)
print(immutable_var[0])
print(immutable_var[2:6:2])
immutable_var[5][1] = 2
print(immutable_var)
# кортеж нельзя изменить потому, что он используетя
# для хранения не изменяемых данных
mutable_list = [7, 8, 9, 'a', 's', 'd']
print(mutable_list)
mutable_list[0] = 'psi'
print(mutable_list)
