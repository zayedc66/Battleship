#Made by Zayed
#3 / 23 / 2023
#Searching and sorting program
import os, time

def bubbleSort(arr):
            n = len(arr)
            # optimize code, so if the array is already sorted, it doesn't need
            # to go through the entire process
            swapped = False
            # Traverse through all array elements
            for i in range(n-1):
                # range(n) also work but outer loop will
                # repeat one time more than needed.
                # Last i elements are already in place
                for j in range(0, n-i-1):
                    # traverse the array from 0 to n-i-1
                    # Swap if the element found is greater
                    # than the next element
                    if arr[j] > arr[j + 1]:
                        swapped = True
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                if not swapped:
                    # if we haven't needed to make a single swap, we
                    # can just exit the main loop.
                    return
                
def binary_search(arr, low, high, x):
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1
    
def add_name():
    os.system('cls')
    ent_name = str(input("Enter a name you would like to add to the list: "))
    os.system('cls')
    bubbleSort(list_name)
    if_on_list = int(binary_search(list_name,0,len(list_name)-1,ent_name))
    if if_on_list == -1:
        list_name.append(ent_name)
    elif not if_on_list == -1:
        print(ent_name,"is already on the list")
    bubbleSort(list_name) 
       
def search_names():
    try:   
        os.system('cls')
  
        binser = input("Enter the name to search (case sensitive!): ")
        os.system('cls')
        bubbleSort(list_name)  
        
        cmnd = int(binary_search(list_name,0,len(list_name)-1,binser))
        
        os.system('cls')
        if not cmnd == -1:
            print(binser,"is number : ",cmnd)
        if cmnd == -1:
            print("Name is not on list, or spelling/case is incorrect...")
       
    except Exception as e:
        print("Name is not on list, or spelling/case is incorrect...")
               
list_name = ["Yeast","Dune","Cris","Ron","Noel", "Noa","Leo", "Mane","Carter","Teerth","Nolon","Bob","Jeff","Aiden","Zach"]
run = True
while run == True:   
    os.system('cls')
    try:    
        os.system('cls')
        print("1) Add A Name To The List: ")
        print("2) Search The List For A Name")
        print("3) Print Current List")
        print("4) Sort The List")
        print("5) EXIT!")
        menu = int(input("Selection: "))
        if menu == 1:
            add_name()
        elif menu == 2:
            search_names()
        elif menu == 3:
            os.system('cls')
            print(list_name)
        elif menu == 4:
            os.system('cls')
            bubbleSort(list_name)
        elif menu == 5:
            os.system('cls')
            exit()
        else:
            raise
        procede = input("Press Enter to Continue: ")
    except:
        os.system('cls')
        print("Not a valid menu selection\n")
        procede = input("Press Enter to Continue: ")

def exit():
    os.system('cls')
    print("okok")
