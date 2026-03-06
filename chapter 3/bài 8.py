nhap = input("Nhập các số, cách nhau bằng khoảng trắng: ")
danh_sach = [float(x) for x in nhap.split()]
tim_thay = False
for so in danh_sach:
    if so > 10:
        print(f"Số đầu tiên lớn hơn 10 là: {so}")
        tim_thay = True
        break
if not tim_thay:
    print("Không có số nào lớn hơn 10 trong danh sách")