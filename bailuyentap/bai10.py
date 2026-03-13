ma = input("mã: ")
ten = input("tên: ")
gia = float(input("giá: "))
with open("danh sach da tao", "a", encoding="utf-8") as file:
    file.write(f"{ma};{ten};{gia}\n")
print("đã lưu")
print("\nDanh sách sp:")
with open("danh sach da tao", "r", encoding="utf-8") as file:
    print(file.read())