student = 1
student_present = 0
student_absent = 0
 
while(student<30):
    status=input("Is the student present or absent: ").lower()
    
    if(status=="present"):
        student_present+=1
    elif(status=="absent"):
        student_absent+=1
    else:
        print("invalid input")

    student+=1

#-----------------------------------------
print("Total students present:",student_present)
print("total students absent:",student_absent)
