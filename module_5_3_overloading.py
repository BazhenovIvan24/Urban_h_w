class House:
    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to(self, new_floor):
        if (new_floor < 1) or (new_floor > self.number_of_floor):
            print('Такого этажа не существует')
        elif new_floor == 1:
            print('Мы на первом этаже')
        else:
            for floor in range(new_floor):
                print(f'Этаж{floor + 1}')

    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return str(f'Название:{self.name}, количество этажей {self.number_of_floor}')

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor

    def  __le__(self,other):
        return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor
    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor

    def __add__(self, value):
        if not isinstance(value, int):
            raise ArithmeticError("Правый операнд должен быть типом int")
        self.number_of_floor += int(value)
        return self

    def __radd__(self, value):
        self.number_of_floor += int(value)
        return self

    def __iadd__(self, value):
        self.number_of_floor += int(value)
        return self


# Далее приведен код для проверки выполнения программы

h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

print(h1)

print(h2)


print(h1 == h2) # __eq__


h1 = h1 + 10 # __add__

print(h1)

print(h1 == h2)


h1 += 10 # __iadd__

print(h1)


h2 = 10 + h2 # __radd__

print(h2)


print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__

