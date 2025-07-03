#Grading System:

marks=float(input("Enter Marks of Student(1-100): "))
if marks>=90 and marks<=100:
    print("the grade is A")
elif marks>=80 and marks<=89:
    print("the grade is B")
elif marks>=70 and marks<=79:
    print("the grade is C")
elif marks>=60 and marks<=69:
    print("the grade is D")
elif marks<=60 and marks>=0:
    print("the grade is F")
else:
    print("invalid input")