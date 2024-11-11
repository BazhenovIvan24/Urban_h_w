first = input()
second = input()
third = input()

if (first == second) or (second == third) or (first == third):
    print(2)
elif first == second == third:
    print(3)
else:
    print(0)