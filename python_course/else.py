cars=["ok","ok","ok","ok","ok"]
for status in cars:
    if status=="faulty":
        print("stopping the production line!")
        break
    print(f"this ca is {status}")
    print("shipping new car to customer")
else:
    print("All cars built successfully. No faulty cars")
