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
				print(f'Этаж{floor+1}')
	def __len__(self):
		return self.number_of_floor
	def __str__(self):
		return str(f'Название:{self.name}, количество этажей {self.number_of_floor}')

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
#h1.go_to(5)
#h2.go_to(10)

		
print(h1)
print(h2)	
			
#print(str(h1)) можно еще так вызвать 
#print(str(h2))				

print(len(h1))
print(len(h2))		
