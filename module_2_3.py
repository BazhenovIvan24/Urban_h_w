my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
k = 0
var1 = my_list[0]
while var1 >= 0:
    if (k + 1) > len(my_list):
        break
    var1 = my_list[k]
    k += 1
    if var1 > 0:
        print(var1)
    elif var1 == 0:
        continue
    else:
        break

