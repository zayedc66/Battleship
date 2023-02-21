#Made by Zayed
#2/21/2023
#Student Average Program
import time, os
menu = True
option1 = False
option2 = False
while menu == True:
    print("option 1)")
    print("option 2)")
    #....
    try: 
        menu_selection = int(input("Selection: "))
        if menu_selection == 2:
            option1 = True
    except:
       print("that is not a valid menu selection, input 1 or 2 or...")