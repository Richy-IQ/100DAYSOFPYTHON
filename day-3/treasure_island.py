#!/usr/bin/python3


print("welcome to the treasure island")
print("your mission is to find the treasure")
step1 = input('you are at a cross road. where do you want to go? type "right" or "left"\n ').lower()
if step1 == "left":
    step2 = input('at this point, you have to "swim" or "wait" to continue the game\n ')
    if step2 == "wait":
        step3 = input('you have to choose the right door to win this game. the options are "red", "blue" and "yellow" \n ')
        if step3 == "red":
            print("you choose the wrong door. game over")
        elif step3 == "blue":
            print("you choose the wrong door. game over")
        elif step3 == "yellow":
            print("you win the game, congratulations to you")
        else:
            print("you choose none of the colors, so game over")
    else:
        print("you caught fire, game over")
else:
    print("you cant go any further, game over")
