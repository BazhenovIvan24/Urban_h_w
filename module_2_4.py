numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes = []
is_prime = True
for n in numbers:
    for delitel in range(2, n):
               
        if n % delitel == 0:
            is_prime = False
            break
    #Check n = 1 or not    
    if n == 1:
            continue    
    if is_prime == False:
        not_primes.append(n)
    else:
        primes.append(n)
    is_prime = True #Обнуляем параметр is_prime (flag)
print(primes)
print(not_primes)
