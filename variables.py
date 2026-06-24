#variable
Name="Mamatha"
Age=18
print(Name)
print(Age)

#local variable
def my_shop():
    toy="teddy"
    print(toy)
my_shop()

#Global variable
toy="Teddy"
def my_shop():
    print(toy)
my_shop()
print(toy)