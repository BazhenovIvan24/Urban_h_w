n = int(input('Введите число: '))

result = []

for i in range(1, n):
    for k in range(1, n):
        if k <= i:
            continue

        delitel = n % (i + k)
        if delitel == 0:
            result.append(i)
            result.append(k)



print(result)  # Вывод списком

for i in range(len(result)):
    result[i] = str(result[i])

print(''.join(result))  #Вывод join строки из получившихся чисел

for x in result:
	print(x)  # Вывод поэлементно

result = tuple(result)

print(result)  # Вывод кортежем


