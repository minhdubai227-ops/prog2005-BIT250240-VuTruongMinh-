import matplotlib.pyplot as plt
products = ["A", "B", "C", "D", "E"]
percent = [30, 25, 15, 20, 10]
plt.pie(percent, labels=products, autopct="%1.0f%%")
plt.title("doanh so sp")
plt.show()