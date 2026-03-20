import matplotlib.pyplot as plt
cities = ["los angeles", "san diego", "san jose", "san francisco", "fresno"]
areas = [1215, 964, 469, 121, 112]
plt.barh(cities, areas, color="lightcoral")
plt.xlabel("(km²)")
plt.title("top tp lon nhat")
plt.gca().invert_yaxis()
plt.show()