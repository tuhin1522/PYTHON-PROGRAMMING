# class Person:
#     def __init__(self, name, sex, profession):
#         self.name = name
#         self.sex = sex
#         self.profession = profession

#     def show(self):
#         print("Name: ", self.name, '\nSex: ', self.sex, '\nProfession: ', self.profession)

#     def work(self):
#         print(self.name, 'working as a', self.profession)

# # Creating an instance of the Person class
# jessa = Person('Tuhin', 'Male', 'Software Engineer')

# # Calling methods on the instance
# jessa.show()
# jessa.work()

# class Student:
#     school_name = 'ABC School'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# # access instance variables
# s1 = Student('Harry',20)
# print("Student: ",s1.name, s1.age)

# # access class variable
# print('School name: ', Student.school_name)

# # Modify instance variables
# s1.name = 'Jessa'
# s1.age = '12'
# print("Student: ",s1.name, s1.age)

# # Modify class variables
# Student.school_name = 'XYZ School'
# print('School name:', Student.school_name)

# class Fruit:
#     def __init__(self,name, color):
#         self.name = name
#         self.color = color
    
#     def show(self):
#         print("Fruit is", self.name,"and Color is", self.color)
    

# obj = Fruit("Banana","Green")
# obj.name = "Strawberry"
# obj.show()

# del obj.name
# print(obj.color)

class Vehicle:
    def __init__(self, engine):
        print("Inside vehicle constructor.")
        self.engine = engine

class Car(Vehicle):
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print('Inside Car Constructor')
        self.max_speed = max_speed

class Electric_Car(Car):
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print('Inside Electric Car Constructor')
        self.km_range = km_range

obj = Electric_Car('1500cc', 240, 750)
print(f'Engine = {obj.engine}, Max Speed = {obj.max_speed}, Distance = {obj.km_range}')  # Fix here
