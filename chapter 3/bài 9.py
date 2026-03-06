nhap = input("Nhập các số, cách nhau bằng khoảng trắng: ")
danh_sach = [float(x) for x in nhap.split()]
so_le = []
for so in danh_sach:
    if so % 2 != 0:
        so_le.append(so)
if so_le:
    print("Các số lẻ trong danh sách:", so_le)
else:
    print("Không có số lẻ nào trong danh sách")