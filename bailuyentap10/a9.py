class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("ko dc rong")
        self._name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("tuoi ko dc am")
        self._age = value
    def greet(self):
        return f"toi la {self.name}"
    @classmethod
    def from_string(cls, s):
        name, age = s.split(",")
        return cls(name, int(age))
    @staticmethod
    def is_adult(age):
        return age >= 18
    def __str__(self):
        return f"{self.name} - {self.age} tuoi"
    def __eq__(self, other):
        return self.age == other.age
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
    def __str__(self):
        return f"{self.name} - {self.age} tuoi - mssv: {self.student_id}"