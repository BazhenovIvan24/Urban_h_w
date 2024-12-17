def get_multiplied_digits(number):
	str_number = str(number)
	
	first = int(str_number[0])


	if len(str_number) == 1:
		return first if first != 0 else 1 # Базовый случай: одна цифра
	else:
		return first * get_multiplied_digits(int(str_number[1:]))

product_of_number = get_multiplied_digits(402030)
print(product_of_number)
