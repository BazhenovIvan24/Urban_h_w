def print_params(a = 1, b = 'строка', c = True):
	print(a, b, c)

values_list = (29, 'string_2', False)
print_params(*values_list)  
values_dict = {'a' : 1, 'b' : 2, 'c' : 3}
print_params(**values_dict) 

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  #print values2 + value = 42


print_params(b = 25)
print_params(c = [1,2,3], a = 2)

