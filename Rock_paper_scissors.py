import os
import random as r

os.system("cls")

def board():
    os.system("cls")
    print("""---------------------
| 1. Rock           |  
| 2. Paper          |
| 3. Scissors       |
---------------------""")

def result(person,computer):
    if person==computer:
        return 0
    elif (person==1 and computer==2) or (person==2 and computer==3) or (person==3 and computer==1):
        return -1
    elif person==1 and computer==3 or (person==3 and computer==2) or (person==2 and computer==1):
        return 1


def result_board(person,computer,p_count,c_count):
    os.system("cls")
    shablon={1:"Rock",2:"Paper",3:"Scissors"}
    print("<<<<<<<<<<<>>>>>>>>>>>")
    print(f" You -> {shablon[person]}          ")

    print(f" Computer -> {shablon[computer]} ")

    if result(person,computer) == -1:
        print("\tYou lose       ")
    elif result(person,computer) == 0:
        print("\tDraw!          ")
    elif result(person,computer) == 1:
        print("\tYou win!       ")
    print(f"    {p_count}    :    {c_count}      ")
    print("<<<<<<<<<<<>>>>>>>>>>>\n")


play=0
person_count=0
computer_count=0
while person_count<3 and computer_count<3:
    board()
    person=int(input())
    if 0<person<4:
        computer=r.choice([1,2,3])
        last_result=result(person,computer)
        if last_result == 1:
            person_count+=1
        elif last_result == -1:
            computer_count+=1
        
        result_board(person,computer,person_count,computer_count)
        next =input("Will you continue?[y/n]")
        if next.lower()=='n':
            break
os.system("cls")
if computer_count>person_count:
    print("YOU ARE LOOOOSSEEEEERR!!!!")
elif person_count>computer_count:
    print("You are winner!!!")
else:
    print("DRAW!!!!")