a = int(input("Nhập sô thứ nhất: "))
b = int(input("Nhâp số thứ hai: "))
while b != 0:
    a, b = b, a % b
print(f"Ước số chung lớn nhất là: {a}")