## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]
is_prime = []

for check in check_prime:
    for i in range(2,check,1):
        print(i)
        if (check % i) == 0:
            print("oln")
            break
        if i == check -1:
            is_prime.append(check)
        
## HINT: You can use the modulo operator to find a factor

print(is_prime)


