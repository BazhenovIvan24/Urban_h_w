
tuple_1 = 1, 2, 3, 4, True  #Не изменяемые объекты внутри, можно хранить объекты разных типов
list_1 = [1, 2, 3, 5, True, 'g', [0, 1, 2]]
print(type(tuple_1))
a = tuple(list_1)
print(a)
print(a.__sizeof__())
change_1 = a[6][1] = 5
print(a)
# Кортеж (tuple) поддерживает операции умножения и конкатенация (сложение строк)
tuple_2 = 1, 2, 3
tuple_2_1 = tuple_2 * 4
print(tuple_2_1)
