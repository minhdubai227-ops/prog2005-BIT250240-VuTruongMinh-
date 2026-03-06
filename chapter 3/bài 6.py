nhap = input("Nhập các số nguyên, cách nhau bằng khoảng trắng: ")
so_nguyen = [int(x) for x in nhap.split()]
print("Danh sách ban đầu:", so_nguyen)
n = len(so_nguyen)
so_lan_hoan_doi = 0
for i in range(n - 1):
    for j in range(n - 1 - i):
        if so_nguyen[j] > so_nguyen[j + 1]:
            so_nguyen[j], so_nguyen[j + 1] = so_nguyen[j + 1], so_nguyen[j]
            so_lan_hoan_doi += 1
print("Danh sách sau khi sắp xếp tăng dần:", so_nguyen)
print(f"Số lần hoán đổi: {so_lan_hoan_doi}")