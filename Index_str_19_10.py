#Напишем код с индексацией и изменением списка
task_19_10 = ['Python_dz', 0]
task_19_10.append('Работа')   #Добавили элемент в конец списка
task_19_10.extend(['Найти статьи', 1])
task_19_10.append(0)
print(type(task_19_10))
task_19_10.remove(0)  #команда remove убирает 1 элемент только из списка (пробегается от 1 до последнего элемента)
print(task_19_10)
#Also we can check the element in ist
a = 'Работа' in task_19_10
b = 'Работа' not in task_19_10
print(a)
print(b)
print(task_19_10[0:4:2] * 5)

# methods for working with strings
name = input('Name: ')    #в команде ввода всегда строка
print(type(name))
current_year = 2024
birthday_year = input('Year: ')
print('mr. '.replace('m', 'M'), name,' Your age is '.upper(), current_year - float(birthday_year))