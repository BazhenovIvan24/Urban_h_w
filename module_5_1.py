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
	
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)


			
		
			
		
