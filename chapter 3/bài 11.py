nhap = input("Nhập các số, cách nhau bằng khoảng trắng: ")
danh_sach = [float(x) for x in nhap.split()]
if danh_sach:
    lon_nhat = max(danh_sach)
    nho_nhat = min(danh_sach)
    print(f"Cách 1 - Giá trị lớn nhất: {lon_nhat}")
    print(f"Cách 1 - Giá trị nhỏ nhất: {nho_nhat}")
    lon_nhat = danh_sach[0]
    nho_nhat = danh_sach[0]
    for so in danh_sach:
        if so > lon_nhat:
            lon_nhat = so
        if so < nho_nhat:
            nho_nhat = so
    print(f"Cách 2 - Giá trị lớn nhất: {lon_nhat}")
    print(f"Cách 2 - Giá trị nhỏ nhất: {nho_nhat}")
else:
    print("Danh sách rỗng")