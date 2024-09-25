my_dict = {'Name': 1, 'born': 1333, 'max': 0}
print(my_dict)
print(my_dict['Name'])
my_dict['action'] = 5
print(my_dict)
my_dict.update({'ron':3333333, 'gari': 55555555})
print(my_dict)
my_dict.pop('born')
print(my_dict)
print(my_dict.get('born'))
print(my_dict)
#
my_set = {1, 1, 3, 10, 55, 55, 14, 646, 'stroka', (1, 2, 3), False}
print(my_set)
print(my_set.add(13))
print(my_set.add('igruha'))
print(my_set)
print(my_set.remove(1))
print(my_set)