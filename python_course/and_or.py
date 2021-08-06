age=int(input("enter your age: "))
can_learn_programming=age>0 and age<150
print "you can learn programming", + can_learn_programming #true r false



age=int(input("enter your age: "))
usually_working=age<18 or age>65

print "at", + age, "you are not usually working", + usually_working



name=input("enter your name: ")
surname=input("enter your surname: ")
greeting=name or "my.", +surname
print(greeting)
