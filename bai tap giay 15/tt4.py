x = float(input("diem so : "))
y = float(input("diem so : "))
z = float(input("diem so : "))
tb = (x+y+z)/3
print(f"diem tb {tb}")
if tb >= 8:
    print("gioi")
elif tb >=6.5-7.9:
    print("kha")
elif tb >=5.0-6.4:
    print("Tb")
elif tb >=5:
    print("yeu")