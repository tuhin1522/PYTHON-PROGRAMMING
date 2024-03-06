class Dog:
    """A simple attempt to model a dog."""
    def __init__(self,name,age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
    
    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

sit()