class Animal:
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("dong vat keu")
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    def sound(self):
        print(f"{self.name} sua : meo meo meo meo meo")
dog = Dog("Mạnhx")
dog.sound()