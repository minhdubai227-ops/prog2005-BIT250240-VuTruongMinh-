so = int(input("chọn sôs từ 1 đến 9: "))
if 1 <= so <= 9:
    for i in range(1, 10):
        print(f"{so} x {i} = {so*i}")
else:
    print("không hợp lệ")