class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
    def kiem_tra_diem(self):
        return 0 <= self.diem <= 10

    def display(self):
        if self.kiem_tra_diem():
            print(f"Sinh viên {self.ten} có điểm là {self.diem}")
        else:
            print(f"Sinh viên {self.ten} có điểm {self.diem} (không hợp lệ)")
sv1 = Student("vũ trường minh", 9.9)
sv2 = Student("trần đức mạnh", 36)
sv3 = Student("le thuy duong",8.8 )
print("danh sach")
sv1.display()
sv2.display()
sv3.display()