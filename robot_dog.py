class Robot_Dog:
    def __init__(self, name_val, breed_val):
        self.name = name_val
        self.breed = breed_val

    def bark(self):
        print("Woof woof!")


# Main program
robot_dog1 = Robot_Dog("Rex", "German Shepherd")
robot_dog2 = Robot_Dog("Buddy", "Golden Retriever")
print(robot_dog1.name)  # Output: Rex
print(robot_dog2.breed)  # Output: Golden Retriever
Robot_Dog.bark(robot_dog1);
robot_dog2.bark();
