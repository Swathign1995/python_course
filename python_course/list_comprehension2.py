#names in lower case
names=["Rolf","Bob","Jen"]
lower=[name.lower() for name in names]
print(lower)




friend=input("Enter your friend name: ")
friends=["Rolf","Bob","Jen","Charlie","Anne"]
friends_lower=[name.lower() for name in friends]


if friend.lower() in friends_lower:
    print(f"{friend} is one of your friends.")


    #whether the i/p is in lower or upper it print
