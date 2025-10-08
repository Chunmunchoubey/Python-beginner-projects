import random
Cnumber = random.randrange(1,101)
userinput = int(input("Enter your number:"))
if userinput > Cnumber:
    print("Computer number", Cnumber)
    print("Your guess number is too high")
elif Cnumber > userinput:
    print("Computer number", Cnumber)
    print("Your guess number is too low")
else:
    print("Computer number", Cnumber)
    print("Your guess number is equal")
    