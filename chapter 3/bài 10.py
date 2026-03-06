nhap = input("Nhập các số, cách nhau bằng khoảng trắng: ")
danh_sach = [float(x) for x in nhap.split()]
so_chan = []
tong_chan = 0
for so in danh_sach:
    if so % 2 == 0:
        so_chan.append(so)
        tong_chan += so
if so_chan:
    print("Các số chẵn trong danh sách:", so_chan)
    print(f"Tổng các số chẵn: {tong_chan}")
else:
    print("Không có số chẵn nào trong danh sách")