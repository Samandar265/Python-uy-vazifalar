import os
import random as r
from webbrowser import get

os.system("cls")

def board():
    os.system("cls")
    print("""---------------------
| 1. Rock           |  
| 2. Paper          |
| 3. Scissors       |
---------------------""")

def result(person,computer):
    if (person==1 and computer==1) or (person==3 and computer==3) or (person==2 and computer==2) :
        return 0
    elif (person==1 and computer==2) or (person==2 and computer==3) or (person==3 and computer==1):
        return -1
    elif person==1 and computer==3 or (person==3 and computer==2) or (person==2 and computer==1):
        return 1


def result_board(person,computer,p_count,c_count):
    os.system("cls")
    print("------------------------")
    if person==1:
        print("| You -> Rock          |")
    elif person==2:
        print("| You -> Paper         |")
    elif person==3:
        print("| You -> Scissors      |")
    if computer == 1:
        print("| Computer -> Rock     |")
    elif computer == 2:
        print("| Computer -> Paper    |")
    elif computer == 3:
        print("| Computer -> Scissors |")

    if result(person,computer) == -1:
        print("|\tYou lose       |")
    elif result(person,computer) == 0:
        print("|\tDraw!          |")
    elif result(person,computer) == 1:
        print("|\tYou win!       |")
    print(f"|     {p_count}    :    {c_count}      |")
    print("------------------------")


play=0
person_count=0
computer_count=0
while person_count<3 and computer_count<3:
    board()
    person=int(input())
    if 0<person<4:
        computer=r.randint(1,4)
        
        if result(person,computer) == 1:
            person_count+=1
        elif result(person,computer) == -1:
            computer_count+=1

        if result(person,computer) == 1 or result(person,computer) == -1:
            play+=1
        
        result_board(person,computer,person_count,computer_count)
        helping=input()
os.system("cls")
if computer_count==3:
    print("YOU ARE LOOOOSSEEEEERR!!!!")
elif person_count==3:
    print("You are winner!!!")