#Made by Zayed
#2/8/2023
#Battleship
#spot=["o"]*25
import os
spot=[]
i=1 
while i<=25:
    spot.append(str(i))
    i+=1
    

run=True
while run:
    i=0
    row=1
    print("___________________________")
    while i<25:
        print(f"|   {spot[i]}   {spot[i+1]}   {spot[i+2]}   {spot[i+3]}   {spot[i+4]}|")
        i+=5
        row+=1
    print("---------------------------")
    guess = (input("Enter a number from 1 to 25: "))
    if guess=="1":
        spot[0]="M"
    if guess=="2":
        spot[1]="M"
    if guess=="3":
        spot[2]="M"
    if guess=="4":
        spot[3]="M"
    if guess=="5":
        spot[4]="M"
    if guess=="6":
        spot[5]="M"
    if guess=="7":
        spot[6]="M"
    if guess=="8":
        spot[7]="M"
    if guess=="9":
        spot[8]="M"
    if guess=="10":
        spot[9]="M"
    if guess=="11":
        spot[10]="M"
    if guess=="12":
        spot[11]="M"
    if guess=="13":
        spot[12]="M"
    if guess=="14":
        spot[13]="M"
    if guess=="15":
        spot[14]="M"
    if guess=="16":
        spot[15]="M"
    if guess=="17":
        spot[16]="M"
    if guess=="18":
        spot[17]="M"
    if guess=="19":
        spot[18]="M"
    if guess=="20":
        spot[19]="M"
    if guess=="21":
        spot[20]="M"
    if guess=="22":
        spot[21]="M"
    if guess=="23":
        spot[22]="M"
    if guess=="24":
        spot[23]="M"
    if guess=="25":
        spot[24]="M"
    print(guess)
    os.system("cls")
