cars=["ok","ok","ok","faulty","ok","ok"]

for status in cars:
    print (f"This car is {status}.")



cars=["ok","ok","ok","faulty","ok","ok"]
for status in cars:
    if status=="faulty":
        print("stopping the production line!")
        break
    print(f"this car is {status}")
    print("shipping new car to customer")


cars=["ok","ok","ok","faulty","ok","ok"]
for status in cars:
    if status=="faulty":
        print("found faulty car, skipping...")
        continue
    print(f"this ca is {status}")
    print("shipping new car to customer")    
    
