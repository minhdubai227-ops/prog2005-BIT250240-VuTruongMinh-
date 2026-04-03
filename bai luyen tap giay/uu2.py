danh_sach_ten=[]
for i in range(5):
    ten = input(f"nhap ten {i+1}: ")
    danh_sach_ten.append(ten)
    print(f"danh sach ten {danh_sach_ten}")
danh_sach_ten.pop(1)
print(f"danh sach xoa ten thu 2 {danh_sach_ten}")