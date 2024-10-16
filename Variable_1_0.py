# Записываем переменные
class HomeWork:
    def __init__(self, quantity_hw, hour):
        self.quantity_hw = quantity_hw
        self.hour = hour

name_of_course = 'Python'
My_result = HomeWork(12, 1.5)
time_for_one_course = My_result.hour / My_result.quantity_hw
print('Курс: ', name_of_course,  ', всего задач: ', My_result.quantity_hw, ', затрачено часов: ', My_result.hour, ', среднее время выполнения', time_for_one_course, 'часа')


