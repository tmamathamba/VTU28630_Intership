'''#for loop
for i in range(6):
    print("Mamatha")

#while loop
count=1
while count <=5:
    print(count)
    count+=2

#nested loop
for i in range(5):
    for j in range(3):
        print("*",end="")
    print()


for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()'''


rows = 5
for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()