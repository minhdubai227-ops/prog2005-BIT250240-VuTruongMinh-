def kiem_tra_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
chuoi = input("chuỗi số (vd: 5;7;8;-2;8): ")
so_list = [int(x.strip()) for x in chuoi.split(';')]
print("số:")
for so in so_list:
    print(so)
so_chan = sum(1 for so in so_list if so % 2 == 0)
print(f"chẵn: {so_chan}")
so_am = sum(1 for so in so_list if so < 0)
print(f"âm: {so_am}")

so_nguyen_to = sum(1 for so in so_list if kiem_tra_nguyen_to(so))
print(f"số nguyên tố: {so_nguyen_to}")