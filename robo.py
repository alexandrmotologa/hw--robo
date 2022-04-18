from os import system
from random import randint

# map size
LENGTH_X = 20
LENGTH_Y = 10

# robo settings
roboX = randint(1, LENGTH_X-1)
roboY = randint(1, LENGTH_Y-1)
robo_score = 0
robo_hp = 100

# bombs coordinates
def bombs(x1, y1, x2, y2):
    bombX_1, bombX_2 = x1, x2
    bombY_1, bombY_2 = y1, y2
    return bombX_1, bombY_1, bombX_2, bombY_2


bombX_1, bombY_1, bombX_2, bombY_2 = bombs(
    randint(1, LENGTH_X-1), randint(1, LENGTH_Y-1),
    randint(1, LENGTH_X-1), randint(1, LENGTH_Y-1))

# coins coordinates
def coins(x1, y1, x2, y2):
    coinX_1, coinX_2 = x1, x2
    coinY_1, coinY_2 = y1, y2
    return coinX_1, coinY_1, coinX_2, coinY_2


coinX_1, coinY_1, coinX_2, coinY_2 = coins(
    randint(1, LENGTH_X-1), randint(1, LENGTH_Y-1),
    randint(1, LENGTH_X-1), randint(1, LENGTH_Y-1))

# heart coordinates
def heart(x, y):
    heartX = x
    heartY = y
    return heartX, heartY


heartX, heartY = heart(randint(1, LENGTH_X-1), randint(1, LENGTH_Y-1))

# clear console    
def clear_console():
    system("cls")
    print()

# game loop
while True:
    # draw map
    clear_console()
    
    print(f"HP: {robo_hp}   SCORE: {robo_score}")
    
    for col in range(1, LENGTH_Y+1):
        for row in range(1, LENGTH_X+1):
            
            # print robo
            if roboX == row and roboY == col:
                print("🤖", end=" ")
                if roboX == heartX and roboY == heartY:
                    if robo_hp < 100:
                        robo_hp += 10
                    heartX, heartY = heart(
                        randint(1, LENGTH_X-1), randint(1, LENGTH_Y-1))
                    
                # print new bomb
                if roboX == bombX_1 and roboY == bombY_1 or roboX == bombX_2 and roboY == bombY_2:
                    if robo_hp > 0 and robo_hp <= 100:
                        robo_hp -= 10
                        robo_score -= 10
                    else:
                        print("game over")
                        exit()
                    if roboX == bombX_1 and roboY == bombY_1:
                        bombX_1, bombY_1, bombX_2, bombY_2 = bombs(
                            randint(1, LENGTH_X-1), randint(1, LENGTH_Y-1),
                            bombX_2, bombY_2)
                    if roboX == bombX_2 and roboY == bombY_2:
                        bombX_1, bombY_1, bombX_2, bombY_2 = bombs(
                        bombX_1, bombY_1,
                        randint(1, LENGTH_X-1), randint(1, LENGTH_Y-1))
                
                # print new coin        
                if roboX == coinX_1 and roboY == coinY_1 or roboX == coinX_2 and roboY == coinY_2:
                    robo_score += 10
                    if roboX == coinX_1 and roboY == coinY_1:
                        coinX_1, coinY_1, coinX_2, coinY_2 = coins(
                            randint(1, LENGTH_X-1), randint(1, LENGTH_Y-1),
                            coinX_2, coinY_2)
                    if roboX == coinX_2 and roboY == coinY_2:
                        coinX_1, coinY_1, coinX_2, coinY_2 = coins(
                            coinX_1, coinY_1,
                            randint(1, LENGTH_X-1), randint(1, LENGTH_Y-1))
            
            # print coins, bombs, heart            
            elif bombX_1 == row and bombY_1 == col:
                print("💣", end=" ")
            elif bombX_2 == row and bombY_2 == col:
                print("💣", end=" ")
            elif heartX == row and heartY == col:
                print("💜", end=" ")
            elif coinX_1 == row and coinY_1 == col:
                print("💵", end=" ")
            elif coinX_2 == row and coinY_2 == col:
                print("💵", end=" ")
            else:
                print(". ", end=" ")
        print()

    # user options
    option = input(">>> ").lower()
    # option = user_input[0]
    if option == "a" and roboX != 1:
        roboX-=1
    if option == "s" and roboY != LENGTH_Y:
        roboY+=1
    if option == "d" and roboX != LENGTH_X:
        roboX+=1
    if option == "w" and roboY > 1:
        roboY-=1