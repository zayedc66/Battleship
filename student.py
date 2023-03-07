#student averages program
#Program by Zayed
#Date: 2 / 21 / 2023
import os
import time
try:    
    Students=[["John","Doe","Passed",80.0,79.0,83.0,72.0,78.5],["Jane","Doe","Passed",83.0,95.0,92.0,94.0,91],["George","Python","Failed",37.0,23.0,51.0,46.0,39.3],["Luke","Skywalker","Passed",19.0,77.0,80.0,83.0,64.8],["Teerth","Panchal","Failed",5.0,15.0,13.0,7.0,10.0]]
    menu = True
    start = False
    add = False
    try:        
                    MATH = float(input("MATH mark %: "))
                    ENGLISH = float(input("ENGLISH mark %: "))
                    HISTORY = float(input("HISTORY mark %: "))
                    GYM = float(input("GYM mark %: "))
                    valid=True
    except:
                    os.system('cls') 
                    valid=False
                    print("please enter marks in numerical format, ##.# or ##")
                    time.sleep(2)
    if valid == True and MATH in range(0,100) and ENGLISH in range(0,100) and HISTORY in range(0,100) and GYM in range(0,100):
                    os.system('cls')
                    student_avg = (MATH + ENGLISH + HISTORY + GYM)/4
                    if student_avg >= 50:
                        passed = "Passed"
                    elif student_avg < 50:
                        passed = "Failed"             
                        print(f_name,l_name,passed,"with an overall mark of: ",student_avg,"%" )
                    confirm = input("Enter 'Y' to add student to database OR Enter 'N' to cancel (will return you to menu!): ").upper()
                    if confirm == "Y":
                        confirm = True
                    else:
                        confirm = False
                        print("Student was not added to list..... Returning to main menu.....")
                        time.sleep(2)
                        valid = False
                        add = False
                        mrks == False
                        menu = True    
                    try:  
                        while confirm == True:
                            os.system('cls') 
                            try:
                                Students.append([f_name,l_name,passed,MATH,ENGLISH,HISTORY,GYM,student_avg ])
                                valid = False 
                                add = False
                                mrks = False
                                menu = True   
                                confirm = False  
                                print("Student added, would you like to view list?")
                                list2 = input("'Y' for yes or 'N' for no: ").upper()
                                if list2 == "Y":
                                    valid = False
                                    mrks = False
                                    add = False                                    
                                    list_stud = True
                                    confirm = False                                    
                                else:
                                    valid = False
                                    add = False
                                    mrks = False
                                    menu = True 
                                    confirm = False                                                                       
                            except:
                                print("Student could not be added!....")
                                valid = False 
                                add = False
                                mrks = False
                                menu = True  
                                confirm = False                                          
                    except:
                            print("Student could not be added!....")
                            time.sleep(2)
                            valid = False
                            add = False
                            mrks = False
                            menu = True 
                            valid = False
                else:
                    os.system('cls')
                    print("One of your marks is out of range, 0 to 100") 
                    time.sleep(2)
        while list_stud == True:
            os.system('cls')
            for row in Students:
                print(f" First Name:{row[0]}\n Last Name:{row[1]}\n {row[2]}\n MATH------>{row[3]}%\n ENGLISH--->{row[4]}%\n HISTORY--->{row[5]}%\n GYM------->{row[6]}%\n STUDENT AVERAGE--->{row[7]}%\n----------------------------") 
            back = input("Press any key to go back to menu...")
            menu = True
            list_stud = False
        while Course_avg == True:
            os.system('cls')
            Math_avg = 0
            English_avg = 0
            History_avg = 0
            Gym_avg = 0
            time.sleep(2)                       
        except:
        print("not a valid selection")            
except:
    print("PROGRAM ENDED")           
    