import name
friends=["swathi","sgn","gn"]

family=["abc","xyz"]
user_name=input("enter your name: ")

if user_name in friends:
    print("Hello, friend")
elif user_name in family:
    print("Hello, family")
else:
    print("I don't know you")
