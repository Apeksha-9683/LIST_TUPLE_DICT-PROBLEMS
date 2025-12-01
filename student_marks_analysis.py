students={}

n=int(input("Enter number of students:"))
i=1

while i<=n:
    name=input("Enter student name:")
    marks=input("Enter student details marks in 3 sub")
    marks=marks.split(',')
    marks_tup=tuple(map(int,marks))
    students[name]=marks_tup
    i+=1
print(students)

for name,marks_tup in students.items():
    total_sum=sum(marks_tup)

    avg=total_sum/len(marks_tup)
    print(f"the student {name} has scored total marks of {total_sum} and an average of {avg}")

    #it would throw an error as 100,23,34 in marks are strings and we are trying to separeate with which is not possible
    #we need to take string input
    '''50 is integer but 100,12,34 is not integer, so take as only input and using mapping and in convert it into tuple of intger values'''


