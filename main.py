#Made by Zayed
#2/8/2023
#Battleship
#spot=["o"]*25
import os
spot=[]
i=1 
while i<=25:
    spot.append("🌊")
    spot.append("🌊")
    spot.append("🌊")
    spot.append("🌊")
    spot.append("🌊")
    i+=1
#HIDDEN_BOARD=[['']*5 for x in range(5)] 
#GUESS_BOARD=[['']*5 for x in range(5)] 
run=True
while run:
    i=0
    row=1
    print("       A    B    C    D    E")
    print("______________________________________")
    while i<25:
        print(f"|{row} |   {spot[i]}  |  {spot[i+1]}  |  {spot[i+2]}  |  {spot[i+3]}  |  {spot[i+4]}|")
        i+=5
        row+=1
    print("--------------------------------------")
    guess = (input("Enter a coordinate(letter, number): ")).upper()
    if guess=="A1":
        spot[0]="💨"
    if guess=="A2":
        spot[1]="💨"
    if guess=="A3":
        spot[2]="💨"
    if guess=="A4":
        spot[3]="💨"
    if guess=="A5":
        spot[4]="💨"
    if guess=="B1":
        spot[5]="💨"
    if guess=="B2":
        spot[6]="💨"
    if guess=="B3":
        spot[7]="💨"
    if guess=="B4":
        spot[8]="💨"
    if guess=="B5":
        spot[9]="💨"
    if guess=="C1":
        spot[10]="💨"
    if guess=="C2":
        spot[11]="💨"
    if guess=="C3":
        spot[12]="💨"
    if guess=="C4":
        spot[13]="💨"
    if guess=="C5":
        spot[14]="💨"
    if guess=="D1":
        spot[15]="💨"
    if guess=="D2":
        spot[16]="💨"
    if guess=="D3":
        spot[17]="💨"
    if guess=="D4":
        spot[18]="💨"
    if guess=="D5":
        spot[19]="💨"
    if guess=="E1":
        spot[20]="💨"
    if guess=="E2":
        spot[21]="💨"
    if guess=="E3":
        spot[22]="💨"
    if guess=="E4":
        spot[23]="💨"
    if guess=="E5":
        spot[24]="💨"
    print(guess)
    os.system("cls")
