#function
def greet():
    print("hai")
greet()


#types of functions 
#built in functions
print("Hello")
print(len("Mamatha"))
print(max(1,3,6))

#user defined function
def temple():
    print("Shiva")
temple()

#1.functions without arguments and without return value
def greet():
    print("Mamatha")
greet()

#2.functions with arguments and without return value
def greet(name):
    print("hai",name)
greet("Mamatha")

#3.functions without arguments and with return value
def get_number():
    return 50
num=get_number()
print(num)

#4.functions with arguments and with return value
def add(a,b):
    return a+b
sum=add(20,40)
print(sum)

#lambda function
square = lambda x:x*x
print(square(5))


#Recurssive function
def countdown(n):
    if n==0:
        print("Done")
    else:
        print(n)
        countdown(n-1)
countdown(3)

#Generator function
def numbers():
    yield 1
    yield 2
    yield 3
for n in numbers():
    print(n)