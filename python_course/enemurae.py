friends=["Rolf","John","Anne"]

counter=0

for friend in friends:
    print(counter)
    print(friend)
    counter=counter+1





for counter, friend in enumerate(friends):
    print(counter)
    print(friend)


print(list(enumerate(friends)))    
print(list(zip([0,1,2], friends))) #both outputs are same
