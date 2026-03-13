class Hoa:
    def __init__(self, ten, mau):
        self.ten = ten
        self.mau = mau
    def __str__(self):
        return f"hoa{self.ten}mau{self.mau}"
hoa = Hoa("den", "trang")
print(hoa)