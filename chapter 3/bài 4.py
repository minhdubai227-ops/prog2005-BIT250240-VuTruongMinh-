so_nguyen = [5, 6, 4, 11, 22, 36, 18]
print("Danh sách ban đầu:", so_nguyen)
so_nguyen.sort()
print("Sau khi sort (tăng dần):", so_nguyen)
so_nguyen.reverse()
print("Sau khi reverse:", so_nguyen)
so_can_dem = 5
so_lan = so_nguyen.count(so_can_dem)
print(f"Số lần xuất hiện của {so_can_dem}: {so_lan}")