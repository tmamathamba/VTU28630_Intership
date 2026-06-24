#left Triangle
print("left Triangle")
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()


#Inverted Triangle
print("Inverted Triangle")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()


#right Triangle
print("right triangle")
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()

#inverted right triangle
print("inverted right triangle")
for i in range(5,0,-1):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()
 

#Pyramid
print("pyramid")
for i in range(5):
    for j in range(5-i-1):
        print(" ",end="") 
    for k in range(i+1):    
        print("*",end=" ")
    print()

#Inverted pyramid
print("Inverted pyramid")
for i in range(5):
    for j in range(i):
        print(" ",end="") 
    for k in range(5-i):    
        print("*",end=" ")
    print()


#Diamond
print("Diamond")
n=5
for i in range(1,n+1):
    print(" " *(n-i)+"* "  * i)
    print()
for i in range(n,0,-1):
    print(" " *(n-i)+"* " * i)
    print() 


#Rectangle
print("Rectangle")
for i in range(3):
    for j in range(3):
        print("*",end="")
    print()

#increasing number
print("Increasing number")
col=1
n=1
for i in range(1,5):
    for j in range(1,col+1):
        print(n,end="")
        n=n+1
    col=col+2
    print()

#square pattern
print("square pattern")
n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()  

n=5
for i in range(3):
    for j in range(n):
        print("*",end="")
    print()

#left triangle
print("Left Triangle")
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

#inverted triangle
print("Inverted triangle")
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print()

#Right triangle:
print("right triangle")
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end="")
    for k in range(1,i+1):
        print("*",end="")
    print()    


#pyramid
print("pyramid")
for i in range(5):
    for j in range(5-i-1):
        print(" ",end="") 
    for k in range(i+1):    
        print("*",end=" ")
    print() 

#inverted pyramid
print("inverted pyramid")
for i in range(5):
    for j in range(i):
        print(" ",end="") 
    for k in range(5-i):    
        print("*",end=" ")
    print()


#number patterns
print("number pattern")
n=int(input("enter the num:"))
for i in range(n):
    for j in range(1,i+1):
        print(j,end="")
    print()

#number pattern
print("number pattern")
for i in range(1,6):
    for j in range(i):
        print(i,end="")
    print()

#alphabet pattern
print("alphabet pattern")
n=int(input("Enter the num:"))
k=ord("A")
print(k)
for i in range(n):
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()


n=int(input("Enter the num:"))
for i in range(n):
    k=ord("A")+i
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()


n=int(input("enter the value:"))
k=ord("A")
print(k)
for i in range(0,n):  #[0,1,2,3....]
    for j in range(0,i+1):
        print(chr(k),end=" ")
    k=k+1
    print(" ")


#rectangle
print("rectangle")
n=int(input("Enter the value:"))

for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()



