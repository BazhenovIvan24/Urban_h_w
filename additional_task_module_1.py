# На вход подаются оценки и имена учеников
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_marks = []
i = 0
#Создадим цикл, который будет записывать в список (list) average_marks - средние оценки студентов.
while i < len(grades):
    average_marks.append(sum(grades[i]) / len(grades[i]))  #append average marks to general list
    sum_i = 0
    i += 1 # increase_i for cycle "while"
#Теперь расставим студентов по порядку, т.к. у каждого студента есть оценки, то и их количество будет равно количеству списков оценкок

length_list_of_student = list(sorted(students))  #Код исправлен

#Создадим список с помощью функции zip()
dict_marks = zip(length_list_of_student, average_marks)
dict_marks = dict(dict_marks)

#Создадим список 1 такой же с помощью цикла.
dict_marks1 = {}
for i in range(len(length_list_of_student)):
    dict_marks1.update({length_list_of_student[i]: average_marks[i]})



print(dict_marks)




