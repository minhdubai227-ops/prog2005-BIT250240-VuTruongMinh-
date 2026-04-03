so_luong = int(input("nhap so luong: "))
mang_so = []

for i in range(so_luong):
   so = int(input(f"nhap so {i+1}: "))
mang_so.append(so)

cac_so_le = []
for so in mang_so:
    if so % 2 !=0:
     cac_so_le.append(so)

print(f"Cac so le {cac_so_le}) va luong so le : {len (cac_so_le)}")
cac_so_le = True
if so < 2:
    la_nguyen_to= False
else:
    for i in range (2,so):
        if so % i == 0:
            la_nguyen = False
            break
if la_nguyen_to:
    cac_so_nguyen_to.append(so)
print(f"cac so nguyen to{cac_so_nguyen_to}")