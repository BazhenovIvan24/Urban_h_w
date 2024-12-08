n = int(input('Введите число: '))
max_var_n = n + 1
result = []
if n > 9:
    max_var_n = 10

for i in range(1, max_var_n):
    for k in range(1, max_var_n):
        if k <= i:
            continue

        delitel = n % (i + k)
        if delitel == 0:
            result.append([i, k])



print(result)