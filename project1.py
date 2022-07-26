# rock paper scissor game

import random


def gamewin(comp,you):
    if comp== you:
        return None

    elif comp=='R':
        if you=='S':
         return False
        elif you=='P':
         return True

    elif comp =='P':
        if you=='R':
         return False
        if you=='S':
         return True

    elif comp=='S':
        if you=='P':
          return False
        if you=='R':
          return True

print("comp turn : rock(R) paper (P) scissor(S) ? ")
randNo = random.randint(1,3)
if randNo == 1:
     comp = 'R'
elif randNo == 2 :
     comp =' P'

elif randNo ==3:
     comp ='S'

you = input("your turn : rock(R) paper(P) scissor(S) ? ")
a = gamewin(comp,you)

print(f"computer chose {comp}")
print(f"you choose {you}")

if a == None:
    print("the game is tie! try once more")
elif a :
    print("you win ! congrats")
else :
    print("you lose!,")
