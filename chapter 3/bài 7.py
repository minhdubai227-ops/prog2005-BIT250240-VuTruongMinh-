nhap = input("Nhập các số, cách nhau bằng khoảng trắng: ")
danh_sach = [float(x) for x in nhap.split()]
tim_so = float(input("Nhập số cần tìm: "))
tim_thay = False
for i in range(len(danh_sach)):
    if danh_sach[i] == tim_so:
        print(f"Tìm thấy {tim_so} tại chỉ số {i}")
        tim_thay = True
        break
if not tim_thay:
    print(f"Không tìm thấy {tim_so} trong danh sách")