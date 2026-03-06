nhap = input("Nhập các số thực, cách nhau bằng khoảng trắng: ")
so_thuc = [float(x) for x in nhap.split()]
print("Danh sách ban đầu:", so_thuc)
for i in range(1, len(so_thuc)):
    key = so_thuc[i]
    j = i - 1
    while j >= 0 and key > so_thuc[j]:
        so_thuc[j + 1] = so_thuc[j]
        j -= 1
    so_thuc[j + 1] = key
print("Danh sách sau khi sắp xếp giảm dần:", so_thuc)