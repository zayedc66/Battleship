#Made by Zayed
#2/21/2023
#Student Average Program
import time, os
menu = True
option1 = False
option2 = False
def adding_a_user():
    input("add users")
    
    
def listing():
    input("add users")
    
    
def show_board():    
    while menu == True:
        menus = {"1":adding_a_user, "2":listing}
        print("option 1)")
        print("option 2)")
        print("option 3)")
        print("option 4)")
        #....
        try: 
            menu_selection = int(input("Selection: "))
            menu_selection= input("PLease enter INput:")
            if menu_selection in menus:
                menus[menu_selection]()
            else:
                print("Please enter a Valid input")
                time.sleep(1)   
            '''if menu_selection == 1:
                option1 = True
            elif menu_selection == 2:
                option2 = True
            elif menu_selection == 3:
                option3 = True
            elif menu_selection == 4:
                option4 = True
            elif menu_selection >= 5 or menu_selection <= 0:
                print("Thats not a valid input")    '''
        except:
            print("that is not a valid menu selection, input 1, 2, 3 or 4...")
run = True
while run:
    show_board()