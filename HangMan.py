word = "saifullah"
chances = 10
GuessAdd = []
done = False

while not done:
    for latter in word:
        if latter.lower() in GuessAdd:
            print(latter, end= " ")
        else:
            print("_", end= " ")
            
    myguess = input(f"your changes is{chances},guess the latter: ")
    GuessAdd.append(myguess.lower())
    if myguess.lower() not in word.lower():
        chances -= 1
        if chances == 0:
            break
        
    done = True
    for latter in word:
         if latter.lower() not in GuessAdd:
            done = False  
            
if done:
    print(f"yes, you have won the game, the word is {word} ")
else:
    print("you loss the game")                  
                