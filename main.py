#guess it right game

import random
randnum= random.randint(1,100)

# print(randnum)

Rguesses= 10

guesses=0

userGuess=None

name=input("Enter Your Name : ")

while userGuess!=randnum:

    userGuess=int(input(f"Guess Number between 1 to 100 (you have {Rguesses} guesses remaining)-> "))  

    Rguesses -= 1

    if (userGuess== randnum):
        print(f"You Guessed the right number '{randnum}' in {guesses} guesses!, You WIN !")
        print(f"Your score {Rguesses} remaining guesses!")

    elif (userGuess<randnum):
        print("You guessed it wrong! the number is larger")

        if (Rguesses==0):
            print("Oops ! no more guesses remaining")
            print(f"{Rguesses} guesses remaining\nNo more guesses remaining you Lose!")
            break

    elif (userGuess>randnum):
        print("You guessed it wrong! the number is smaller")

        if (Rguesses==0):
            print(f"{Rguesses} guesses remaining\nNo more guesses remaining you Lose!")
            break
            

    
    guesses += 1

with open ('hiscore.txt') as f:
    hiscore = int(f.read())


if Rguesses>hiscore:
    
    with open ('hiscore.txt','w') as f:
        f.write(str(Rguesses))
    with open ('hiname.txt','w') as g:
        g.write(name)

with open ('hiscore.txt') as f:
    hiscore1 = int(f.read())
with open ('hiname.txt') as g:
    hiname = g.read()


print(f"highest score is {hiscore1} remaining guesses by {hiname}")
    


