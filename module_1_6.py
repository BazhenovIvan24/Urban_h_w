#Module_1_6_dictionary
my_dict = {'Ivan': 2001, 'Vera': 2003, 'Lyusya': 2024}
print(f' Dict: {my_dict}')
print(f' Existing value: {my_dict['Ivan']}')
missing_value = my_dict.get('missing_key', 'None')

print(f'Not existing value: , { missing_value}  ')
my_dict.update({'Alex': 2000, 'Don': 1999})

value = my_dict.pop('Alex')
print('Deleted value:', value)
print(f'Modified dictionary: {my_dict}')


#Work with set
my_set = {1, 'Яблоко', 2.3, 1, (1, 2, 3)}
print('Set:', my_set)
#
my_set.add('text_1')
my_set.add('text_2')
my_set.remove((1, 2, 3))
print(f'Modified set: {my_set}')


