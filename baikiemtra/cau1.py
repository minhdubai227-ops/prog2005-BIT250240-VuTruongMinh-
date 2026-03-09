a, b, c = 3,5,7
print(f"Min = {min(a, b, c)}")
print(f"Max = {max(a, b, c)}")
delta = b**2 - 4*a*c
if delta < 0:
 print("pt vo nghiem")
elif delta == 0:
 print(f"nghiem kep: x = {-b/(2*a)}")
else:
 x1 = (-b + math.sqrt(delta)) / (2*a)
 x2 = (-b - math.sqrt(delta)) / (2*a)
 print(f"x1 = {x1:.2f}, x2 = {x2:.2f}")