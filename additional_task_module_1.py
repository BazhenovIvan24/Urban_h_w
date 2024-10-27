# На вход подаются оценки и имена учеников
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
average_marks = []
i = 0
sum_i = 0 #reset the sum of the marks
#Создадим цикл, который будет записывать в список (list) average_marks - средние оценки студентов.
while i < len(grades):
    grades_i = (len(grades[i])) #length list of number of marks (student_i)

    for k in range(grades_i):
        sum_i += grades[i][k]   #sum of marks

    average_marks.append(sum_i / len(grades[i]))  #append average marks to general list
    sum_i = 0
    i += 1 # increase_i for cycle "while"

#Теперь расставим студентов по порядку, т.к. у каждого студента есть оценки, то и их количество будет равно количеству списков оценкок
students_list = list(students)

#Данные об алфавите хранятся в кодировке ASCII, будем использовать функцию ord
# students_alphavite = []
# s = ''
# for character in range(ord('A'), ord('Z')+1):
#     for i in range(len(students_list)):
#         if students_list[i][0] == character:
#             students_alphavite.append(students_list[i])
#     s += chr(character)
# print(students_alphavite)
# print(students_list[0][0])
# print(s)
#почему-то не заработало так, так что просто применим функцию sorted)

students_alphavite_sort = sorted (students_list)


#Теперь есть 2 списка, в одном средние баллы, в другом есть имена по алфавиту.
dict_marks = {}
for i in range(len(students)):
    dict_marks.update({students_alphavite_sort[i]: average_marks[i]})

print(dict_marks)





