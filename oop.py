class ClubMembers:
    def __init__(self, name, birthday, age, favorite_food, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.favorite_food = favorite_food
        self.goal = goal
    
    def display1(self):
        print("Name:", self.name)
        print("Birthday:", self.birthday)
        print("Age:", self.age)
        print("Favorite Food:", self.favorite_food)
        print("goal:", self.goal)

# class ClubOfficers:
#     def __init__(self, name, birthday, age, favorite_food, goal, position):
#         self.position = position
#         ClubMembers.__init__(self, name, birthday, age, favorite_food, goal)

#     def display2(self):
#         print("Name:", self.name)
#         print("Birthday:", self.birthday)
#         print("Age:", self.age)
#         print("Favorite Food:", self.favorite_food)
#         print("goal:", self.goal)
#         print("Position: ", self.position)

m1 = ClubMembers("brix", "april 18", 24, "adobo", "Developer")
# m2 = ClubOfficers("john", "feb 14", 14, "sisig", "Cybersec", "President")

m1.display1()
# m2.display2()