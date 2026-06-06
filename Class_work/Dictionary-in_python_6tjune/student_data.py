#to creat a dictionary to store student's data
students = {'std101':"Akash",'sta102':"Abhinav",'std103':"Anil",'std104':"rahul"}
#to display the data
print("student details :")
print(students)
print("-------------------------------------------")
#to update record of student whose roll number is std103
students['std105']='rohit'
#to update record of student whose roll number is std105
students['std105']='Rakesh'
print("student detail :")
print(students)
print("------------------------------------------------")
for x in students:
    print(x,'->',students[x])