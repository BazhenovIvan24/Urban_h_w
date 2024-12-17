def divide(first, second):
	if (second == 0) and (first > 0):
		return(float('inf'))
	elif (second ==0) and (first <0):
		return(float('-inf'))
	elif (second == 0) and (first == 0):
		return 'Are you nuts? \nGive me normal number.'
	else:
		return first/second 

#test_1 = print(divide(1, 0))
#test_2 = print(divide(-1, 0))
#test_3 = print(divide(1,1))
#test_4 = print(divide(0, 0))


