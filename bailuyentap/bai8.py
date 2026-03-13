class Student:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem

    def kiem_tra_diem(self):
        if 0 <= self.diem <= 10:
            return True
        else:
            return False
sv1=Student("vũ trường minh", 9.9)
sv2=Student("trần đức mạnh", 36)
sv3=Student("le thuy duong", -18)
print(f"Sinh viên {sv1.ten}: {'Hợp lệ' if sv1.kiem_tra_diem() else 'Không hợp lệ'}")
print(f"Sinh viên {sv2.ten}: {'Hợp lệ' if sv2.kiem_tra_diem() else 'Không hợp lệ'}")
print(f"Sinh viên {sv3.ten}: {'Hợp lệ' if sv3.kiem_tra_diem() else 'Không hợp lệ'}")