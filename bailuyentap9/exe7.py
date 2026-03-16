class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, string):
        name, age = string.split('-')
        return cls(name, int(age))
    def __str__(self):
        return f"Tên: {self.name}, Tuổi: {self.age}"
person = Person.from_string("minh-19")
print(person)