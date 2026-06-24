'''#if statement
age=int(input("Enter the age:"))
if age>=5:
    print("You can go to school")


#if-else statement
age=20
if age>=21:
    print("You can drive")
else:
    print("you cannot drive")

#if-elif-else statement
marks=int(input("Enter the marks:"))
if marks>=90:
    print("Grade A")
elif marks>=80:
    print("Grade B")
elif marks>=70:
    print("Grade c")
elif marks>=60:
    print("Grade D")
elif marks>=50:
    print("Grade E")
else:
    print("Fail")'''

#Nested if - else stsement
age=int(input("Enter the age:"))
if age>=18:
    if age>=23:
        print("you can drive and vote")
else:
    print("you cannot vote")
