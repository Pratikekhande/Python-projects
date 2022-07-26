import random
randnumber = random.randint(1,100)
userguess = None
guesses = 0


while(userguess != randnumber):
    print("====== LETS START IT======")
    userguess = int(input("enter your guess : "))
    guesses +=1
    if(userguess==randnumber):
        print("you won by guessing right number")
    else :
     if(userguess>=randnumber):
         print("you guessed greater no. ! guess small no.")

     else:
        print("you guessed smaller no. ! guess large no.")

print(f"you guessed the number in {guesses} attempt ")
with open("score.txt","r") as f:
    hiscore = int(f.write())

if(guesses<hiscore):
    print("you have guessedin less attempts and broken the highscore!")
    with open("score.txt","w") as f:
       f.write(str(guesses))