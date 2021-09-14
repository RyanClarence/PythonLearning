#Input users and print out on terminal

students = {}
number_of_student = input("Eneter Number Of Student : ")
if number_of_student.isdigit() == True:
    for i in range(int(number_of_student)):
        student_name = input("Eneter Student Name :\t")
        student_id = input("Enter Stundent ID :\t")
        students[student_id]=student_name
else:
    print("Digits allowed only")

print("\n\n")
print("*"*40)
print("STUDENT ID","\t\t","STUDENT NAME")
print("*"*40)

for s_id in students:
    print(s_id,"\t\t\t",students[s_id])

print("*"*40)