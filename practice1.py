'''#variables
#Storing name
name=int(input("Enter the name:"))

#swap two numbers using a temporary variable
a=4
b=5
temp=a
a=b
b=temp
print("a:",a)
print("b:",b)

#swap two numbers without using a temporary variable
a=10
b=5
a,b=b,a
print("a:",a)
print("b:",b)

#sum of two variables
a=int(input("ENter the value1:"))
b=int(input("Enter the value2:"))
c=a+b
print("c:",c)

#Area of rectangle
length=int(input("Enter the value:"))
width=int(input("Enter the value:"))
Area=length*width
print("Area:",Area)'''


#Datatypes
'''#Datatype of a given variable
a="mamatha"
print(type(a))

#convert an integer into a float
a=int(input("Enter the value:"))
b=float(a)
print("a:",a)
print("b:",b)

#convert a string into an integer
a="30"
b=int(a)
print("a:",a)
print("b:",b)

#Types of Datatypes
#integer
a=12
print("a:",a)

#Float
b=1.23
print("b:",b)

#String
c="Mamatha"
print("c:",c)

#list
Names=["Bhanu","Mamatha","Ahalya"]
Names.append("Rithika")
Names[1]="Nikitha"
print("Names:",Names)

#tuple
Colors=("Red","Black","Blue")
Colors=Colors+("pink",)
print("Colors:",Colors)

#set
num={1,2,3}
print("num:",num)

#Dictionary
student={
    "Name" :"Mamatha",
    "Age":19,
    "Department" : "Cse"
}
print("Name:",student["Name"])
print("Age:",student["Age"])
print("Department:",student["Department"])

#operators
#sum,difference,product,quotient
n1=int(input("Enter the value of n1:"))
n2=int(input("Enter the value of n2:"))
sum=n1+n2
Difference=n1-n2
product=n1*n2
quotient=n1/n2
print("sum:",sum)
print("Difference:",Difference)
print("product:",product)
print("quotient:",quotient)

#even or odd
n=int(input("Enter the value:"))
if n%2==0:
    print("Even number")
else:
    print("Odd number")

#find the remainder 
n=int(input("Enter the value of n:"))
m=int(input("Enter the value of m:"))
Remainder=n%m
print("Remainder:",Remainder)

#Relational operator
n=int(input("Enter the value of n:"))
m=int(input("Enter the value of m:"))
equal=n==m
Notequal=n!=m
Greater=n>m
Lesser=n<m
Greaterthan=n>=m
lesserthan=n<=m
print("equal:",equal)
print("Notequal:",Notequal)
print("Greater:",Greater)
print("Lesser:",Lesser)
print("Greaterthan:",Greaterthan)
print("lesserthan:",lesserthan)'''

#logical operator
n=int(input("Enter the num:"))
if n>=10 and n<=50:
    print("It is present")
else:
    print("It is absent")


