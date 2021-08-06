numbers=[1,2,3,4,5,6,7,8,9,10]
tables={
        num:num*i for num in range(1,3)
        for i in numbers
 }
print(tables)
