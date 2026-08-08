class Dog:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def bark(self):
        print("bark")


class Cat:
    def __init__(self, name, color="None"):
        self.name = name
        self.color = color


jerry = Dog("Jerry", "labrador")

jerry.type
jerry.bark()

tom = Cat("Tom")
tom.name
tom.color