my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
k = 0

while k <= (len(my_list)-1):
    var1 = my_list[k]
    
    if var1 > 0:
        print(var1)
    elif var1 == 0:
        k += 1
        continue
    else:
        break
    k += 1
	
	

