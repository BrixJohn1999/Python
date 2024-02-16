class Customers:
    greeting = "Welcome to the Coffee Place"

c_1 = Customers()
c_1.name = str(input("Enter your name: "))
c_1.beverage = "Iced caffe latte"
c_1.food = "Cinnamon"
c_1.total = "225"



print(Customers.greeting + c_1.name)
print("NAME: " + c_1.name)
print(c_1.beverage)
print(c_2.food)