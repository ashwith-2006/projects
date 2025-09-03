# snake_water_gun game
import random

comp = random.choice([-1, 0, 1])
youstr = str(input("Enter your choice(snake:s, water:w, gun:g): "))
youdict = {"s" : -1, "w" : 0 , "g" : 1}
reversedict = {-1 : "snake", 0 : "water", 1 : "gun"}

you = youdict[youstr] 

print(f"you chose {reversedict[you]} \n computer chose {reversedict[comp]}")

if you == comp:
    print("It's a tie!")

else:
    if(comp == -1 and you == 0 ) or (comp == 0 and you == 1) or (comp == 1 and you == -1):
        print("You lose!")
    elif (comp == -1 and you == 1) or (comp == 0 and you == -1) or (comp == 1 and you == 0):
        print("You win!")
        
    else:
        print("Invalid input, please enter s, w, or g.")
  
