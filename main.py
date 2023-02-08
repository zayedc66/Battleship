#Made by Zayed
#2/8/2023
#Battleship

spot=["o"]*25
run=True
while run:
    i=0
    row=1
    print("| A B C D E|")
    print("----------------")
    print("__________________________________________")
    while i<25:
        print(f"|   {spot[i]}   {spot[i+1]}   {spot[i+2]}   {spot[i+3]}   {spot[i+4]}|")
        i+=5
        row+=1
    print("----------------")
    guess = int(input("Enter a spot number: "))
    spot[guess]="M"
    print(guess)