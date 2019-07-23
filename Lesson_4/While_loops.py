# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

# track the current number being multiplied
current = 1

while current <= number:
    
    # multiply the product so far by the current number
    product *=current
    
    # increment current with each iteration until it reaches number
    current += 1


# print the factorial of number
print(product)


# number to find the factorial of
number = 6   

# start with our product equal to one
product = 1

for num in range(1,number+1,1):
    product *= num



print(product)

start_num = 1
end_num = 100
count_by = 3

break_num = start_num

while break_num < end_num:
    break_num += count_by



print(break_num)

start_num = 8
end_num = 5
count_by = 3

break_num = start_num
result = ""
if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
     
    result = break_num
print(result)


#Find the nearest square that is nearest variable limit
limit = 40

nearest_square = 1
num = 1
iteration = 1
last_value = 0

while num < limit:

    num = iteration*iteration
    
    if num < limit:
       last_value = num
    
    iteration += 1 
      
 

nearest_square = last_value

print(nearest_square)
