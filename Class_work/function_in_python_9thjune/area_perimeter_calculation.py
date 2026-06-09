'''create a python program which provides a menu to th user to select the twpo D figure()
after selecting the figure user a again to select a 
provide the imput of corresponding data from figure
 after input a coressponding data again provide a menu to select the operation area.,
 perimeter as per the data provided by the user display the resul of operation . 
 the task will be repeated again and again until user select the option to exit from that figure.'''

import twodfigures

while True:
    print("MENU")
    print("CIRCLE")
    print("RECTANGLE")
    print("SQUARE")
    print("EXIT")

    choice=int(input("enter your choice"))
    
    if choice==4:
        print("Program Ended")
        break

    elif choice==1:
        r=int(input("Enter radius: "))
        while True:
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Circle")

            op=int(input("Enter operation: "))

            if op==1:
                print("Area=",twodfigures.circle_area(r))
            elif op==2:
                print("Perimeter=",twodfigures.circle_perimeter(r))
            elif op==3:
                break
            else:
                print("Invalid Choice")
        
    elif choice==2:
        l=int(input("Enter length: "))
        b=int(input("Enter breadth: "))

        while True:
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Rectangle")

            op = int(input("Enter operation: "))

            if op==1:
                print("Area =", twodfigures.rectangle_area(l, b))
            elif op==2:
                print("Perimeter =", twodfigures.rectangle_perimeter(l, b))
            elif op==3:
                break
            else:
                print("Invalid Choice")

    elif choice==3:
        side=int(input("Enter side: "))

        while True:
            print("1. Area")
            print("2. Perimeter")
            print("3. Exit Square")

            op = int(input("Enter operation: "))

            if op == 1:
                print("Area =", twodfigures.square_area(side))
            elif op == 2:
                print("Perimeter =", twodfigures.square_perimeter(side))
            elif op == 3:
                break
            else:
                print("Invalid Choice")

    else:
        print("Invalid Choice")