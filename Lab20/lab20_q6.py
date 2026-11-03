students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
total=0
top_name,top_score=students[0]
bottom_name,bottom_score=students[0]
for name, score in students:
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="Fail"
    print(name,":",score,grade)
    total+=score

    if score>top_score:
        top_score=score
        top_name=name
    if score<bottom_score:
        bottom_score=score
        bottom_name=bottom_name

average=total/len(students)
print("average is ",average)

print("The top scorer is ", top_name, "with a score of ", top_score)
print("The bottom scorer is ", bottom_name, "with a score of ", bottom_score)