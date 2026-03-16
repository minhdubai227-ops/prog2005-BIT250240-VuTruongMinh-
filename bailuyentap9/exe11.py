class SinhVien:
    count = 0
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
        SinhVien.count += 1
    def __eq__(self, other):
        return self.diem == other.diem
    def __str__(self):
        return f"{self.ten}: {self.diem} diem"
    @classmethod
    def so_luong(cls):
        return f"so sinh vien: {cls.count}"
print(SinhVien.so_luong())
sv1 = SinhVien("trminh", 9.9)
sv2 = SinhVien("manh", 1.8)
print(SinhVien.so_luong())
sv3 = SinhVien("thminh", 3.6)
print(SinhVien.so_luong())