immutable_var =(1, 2, 'a', 'b')
print(immutable_var)
change_immutable_var = immutable_var + (2, 3, 'c', 'd')
change_immutable_var1 = change_immutable_var * 2
#print(change_immutable_var1 )

immutable_var =(1, [2, 3, 4], 'a', 'b')
immutable_var[1][2] = 2 ** 3
#print(immutable_var)

mutable_list = [1, 2, 'a']
mutable_list.append('b')
mutable_list.extend('c1')
mutable_list.remove('c')
mutable_list.remove('1')
mutable_list.append('Modified')


print(mutable_list)

print('Tuple(Кортеж) - неизменяемый объект. \nПоддерживает 2 вида операций - конкатенация и умножение')
