class SinhVien:
    def __init__(self, ten, diem):
        self.ten = ten
        self.diem = diem
    def __eq__(self, other):
        return self.diem == other.diem
    def __str__(self):
        return f"{self.ten}: {self.diem} diem"
sv1 = SinhVien("trminh", 9.9)
sv2 = SinhVien("manh", 3.6)
sv3 = SinhVien("thminh", 1.8)
print(f"{sv1} == {sv2}: {sv1 == sv2}")
print(f"{sv1} == {sv3}: {sv1 == sv3}")