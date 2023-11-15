answer = input("do you want to play the game? [y/n]: ")

if answer == "y":
    print("welcome to the game!")
    answer = input("do you want to go jungle or cave? [jungle/cave]: ")
    if answer == "jungle":
        print("you see the hungry tiger 🙄 tiger will eat you!")
    elif answer == "cave":
        print("you see the bear in front of cave!")
        answer = input("do you want to fight with the bear or run away [fight/run]")
        if answer == "fight":
            print("bear is too much strong! you lose the game")
        else:
            print("wow! still you are alive!")    
else:
    print("The Game closed")
        