tmi = [5, 6, 1, 3, 2, 4]
def b_sort(ls):
	swapped = True
	while swapped:
		swapped = False
		for i in range(len(ls)-1):
			if ls[i]>ls[i+1]:
				ls[i], ls[i+1] = ls[i+1], ls[i]
				swapped = True
	return ls
b_sort(tmi)

print(tmi)



def selection_sort(ls):
	for i in range(len(ls)):
		lowest = i
		for j in range(i+1, len(ls)):
			if ls[j] < ls[lowest]:
				lowest = j
		ls[i], ls[lowest] = ls[lowest], ls[i]

tmi = [5, 6, 1, 3, 2, 4]
selection_sort(tmi)
print(tmi)
