numbers=[0,1,2,3,4]
doubled_numbers=[]

for number in numbers:
    doubled_numbers.append(number * 2)

print(doubled_numbers)    
 


#or we have other method also
numbers=[0,1,2,3,4]
doubled_numbers=[number*2 for number in numbers]
print(doubled_numbers)

#instead of putting in variable
doubled_numbers=[number*2 for number in range(5)]
print(doubled_numbers)



