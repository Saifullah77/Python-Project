import random 

randomnumber = random.randrange(1,200)

userinput = int(input("Guess the number:"))

if userinput > randomnumber :
    print("too high")
elif randomnumber > userinput :
    print("randomnumber")
    print("too low")
    
else:
    print("randomnumber")
    print("yes, you matched the number")
            