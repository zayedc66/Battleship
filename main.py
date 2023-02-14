#Made by Zayed
#2/8/2023
#Battleship
#spot=["o"]*25
import os, random, time
spot=[]
def start_game():
    #this method allows me to set all the spots on the board as the wave emoji
    spot=[]
    i=1 
    while i<=25:
        spot.append("🌊")
        spot.append("🌊")
        spot.append("🌊")
        spot.append("🌊")
        spot.append("🌊")
        i+=1
    return spot


def place_ships():
    ships=["M"]*25
    ship_1=random.randint(1,11)
    ship_2=random.randint(1,11)
    while ship_1 ==ship_2:
        ship_2=random.randint(1,11)
    if ship_1 ==1 or ship_2==1:
        ships[0]="H"
        ships[1]="H"
    if ship_1 ==2 or ship_2==2:
        ships[5]="H"
        ships[10]="H"
    if ship_1 ==2 or ship_2==2:
        ships[6]="H"
        ships[11]="H"    
    if ship_1 ==2 or ship_2==2:
        ships[23]="H"
        ships[24]="H"
    if ship_1 ==2 or ship_2==2:
        ships[21]="H"
        ships[11]="H"
    if ship_1 ==2 or ship_2==2:
        ships[16]="H"
        ships[13]="H"
    if ship_1 ==2 or ship_2==2:
        ships[23]="H"
        ships[19]="H"
    if ship_1 ==2 or ship_2==2:
        ships[3]="H"
        ships[12]="H"
    if ship_1 ==2 or ship_2==2:
        ships[2]="H"
        ships[5]="H"
    if ship_1 ==2 or ship_2==2:
        ships[17]="H"
        ships[18]="H"
    if ship_1 ==2 or ship_2==2:
        ships[13]="H"
        ships[17]="H"
    if ship_1 ==2 or ship_2==2:
        ships[7]="H"
        ships[9]="H"
    return ships 
            
def display_board():
    i=0
    row=1
    print("|      A      B      C      D      E  |")
    print("|-------------------------------------|")
    while i<25:
        print(f"|{row} |   {spot[i]}  |  {spot[i+1]}  |  {spot[i+2]}  |  {spot[i+3]}  |  {spot[i+4]}|")
        i+=5
        row+=1
          
        
def garbage_input():
    print("Bad Input")
    time.sleep(2)



spot=start_game()
ships=place_ships()
run=True
while run:
    display_board()
    guess=input("Enter a coordinate(letter, number): ").upper()
    letter = guess[0]
    number = guess[1]   
    if int(number) <=5:
            if letter == "a":
                start = 0
            if letter == "b":
                start = 1
            if letter == "c":
                start = 2
            if letter == "d":
                start = 3
            if letter == "e":
                start = 4
            if len(guess)<1:
                garbage_input()
            elif guess=="N":
                spot=start_game()
                ships=place_ships()
            elif guess=="Q":
                run=False
                print("Thank you for playing!!")
                time.sleep(2)
            elif not guess[1].isnumeric():
                garbage_input()
            elif int(guess[1])>5:
                garbage_input()
            elif ord(guess[0])>=65 and ord(guess[0])<=69:
                start=ord(guess[0])-65
                spot[start+(int(guess[1])-1)*5]=ships[start+(int(guess[1])-1)*5]
            print(guess)
            os.system("cls")
            

    
'''
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
'''