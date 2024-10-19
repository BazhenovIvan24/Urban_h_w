my_string = input()
def find_len(str):
    count = 0
    while str[count:]:
        count += 1
    return count
len_my_string = find_len(my_string)

print(len_my_string)
#print(len(my_string))
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ', ''))
print(my_string[0])
print(my_string[len(my_string)-1])
