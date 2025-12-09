class Robot:

    def __init__(self, name):
        self.name = name
        self.position = [0, 0]
        print("My name is", self.name + ".")

    def walk(self, x):
        self.position[0] = self.position[0] + x
        self.position[0, 0] = self.position[0, 0] + (x * 2)
        print(self.name, "is now at position", self.position)


class Robot_Dog(Robot):
    def bark(self):
        print("Woof! Woof!")


My_Robot = Robot_Dog("Rex")
My_Robot.walk(5)
My_Robot.bark()
