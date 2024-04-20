import time
import random 
speed = 0
boost = 1
hp = 100
dist = 400

while True:
    print("игра идет")
    if dist <= 0:
        print("\n ура win")
        break
    
    rand = random.randint(1,10)
    if rand == 1:
        print("дерево чо делать")
        Choice = input("1. вправо\n2. влево\n3. прыгнуть")
        trueChoice = random.randint(1,1)
        trueChoice = str(trueChoice)
        print(trueChoice)
        if Choice == trueChoice:
            print("минус дерево")
        else :   
            print("дерево")
            hp = hp - 5
            time.sleep(1)
    elif rand ==2:
        print("йети")
        hp = hp-7
    elif rand ==3:
        print("камень")
        hp = hp - 3
    
    
    dist = dist - speed
    speed = speed + boost
    print(f"\n у вас ост {hp} хп")
    print(f"\ осталось {dist}  метров")
    print(f" ваша скорость {speed} м/с")
    time.sleep(0.5)
