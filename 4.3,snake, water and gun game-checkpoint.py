#hi am pramod
#waiting for run the programm

import random
name=["snake","water","gun"]
computer_choice   =   []
gamer_choice      =   []
win_computer      =   []
win_gamer         =   []

def com():
    a= random.choice(name)
    computer_choice.append(name.index(a))
    print(f"computer selected number : {name.index(a)}")
    return a
def user():
    a=input()
    if a== "0" or a == "1" or a=="2":
        gamer_choice.append(int(a))
        print(f"user selected number : {int(a)}")
        return name[int(a)]
    else:
        user()

def loop():        
        while len(gamer_choice)<=10 :
            a=user()
            b=com()
            if a=="snake" and b == "gun":
                print("computer wins")
                print(f"compter selected : {b} and user selected : {a}")
                win_computer.append(1)
            elif a=="water" and b=="snake":
                print("computer wins")
                print(f"compter selected : {b} and user selected : {a}")
                win_computer.append(2)
            elif a=="gun" and b=="water":
                print("computer wins")
                print(f"compter selected : {b} and user selected : {a}")
                win_computer.append(3)
            elif a=="gun" and b == "snake":
                print("user wins")
                print(f"compter selected : {b} and user selected : {a}")
                win_gamer.append(1)
            elif a=="snake" and b=="water":
                print("user wins")
                print(f"compter selected : {b} and user selected : {a}")
                win_gamer.append(2)
            elif a=="water" and b=="gun":
                print("user wins")
                print(f"compter selected : {b} and user selected : {a}")
                win_gamer.append(3)
            elif a=="water" and b=="water":
                print("same names so plase enter another number")
                print(f"compter selected : {b} and user selected : {a}")
                loop()
            elif a=="snake" and b=="snake":
                print("same names so plase enter another number")
                print(f"compter selected :  {b} and user selected : {a}")
                loop()
            elif a=="gun" and b=="gun":
                print("same names so plase enter another number")
                print(f"compter selected : {b} and user selected : {a}")
                loop()
def final():
    loop()
    print(len(win_computer),":times computer wins")
    print(len(win_gamer),":times user wins")
    if len(win_computer)>len(win_gamer):
        print("computer wins over the user ")
    else:
        print("user wins over computer")
final()
