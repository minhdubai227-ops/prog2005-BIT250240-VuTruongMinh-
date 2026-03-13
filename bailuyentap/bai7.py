class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
sv1 = Student("vũ trường minh", 9.9)
sv2 = Student("trần đức mạnh", 3.6)
print("Đã tạo ")
print(f"Sinh viên 1: {sv1.ten} - {sv1.diem} điểm")
print(f"Sinh viên 2: {sv2.ten} - {sv2.diem} điểm")