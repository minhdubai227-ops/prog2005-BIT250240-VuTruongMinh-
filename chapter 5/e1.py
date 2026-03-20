import matplotlib.pyplot as plt
categories = ["xuat sac", "gioi", "tb", "yeu", "cui bap"]
values = [6, 10, 12, 4, 1]
plt.bar(categories, values, color="skyblue")
plt.title("kq")
plt.xlabel("xep loai")
plt.ylabel("so luong")
plt.show()