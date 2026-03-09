def mark_managment(num):
    student_mark=[]
    for i in range(num):
        number=int(input(f"mark for student{i+1}="))
        student_mark.append(number)
    return student_mark

a=int(input("total student="))
mark=mark_managment(a)
print("mark=",mark)
mark.sort(reverse=True)
print("sorted mark=",mark)
print("highest mark=",max(mark))
print("lowest mark=",min(mark))
avg=sum(mark)/len(mark)
print("average of mark=",avg)
print("top 3 student mark=",mark[:3])


print("\n***Grading system***")
for i in mark:
    if i>=80:
        grade="A+"
    elif i>=70:
        grade="A"
    elif i>=60:
        grade="A-"
    elif i>=50:
        grade="B"
    else:
        grade="F"

    print(f"mark {i}=Grade {grade}")
    