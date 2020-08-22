class Pet:

    number_of_pets = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Pet.count_pets()
    
    
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old', end=" ")

    @classmethod
    def count_pets(cls):
        cls.number_of_pets += 1

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    @staticmethod
    def speak():
        print("Meow!!")
    
    def info(self):
        self.show()
        print("and I am a cat!!")



class Dog(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    @staticmethod
    def speak():
        print("Bark!!")
    
    def info(self):
        self.show()
        print("and I am a dog!!")


tom = Cat("Tom", 12, "blue")
james = Dog("James", 12, "ash")

tom.speak()
james.info()
tom.info()

