import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-2, 2, 100)
plt.plot(x, x**2, "b", label="y = x^2")
plt.plot(x, x**3, "r", label="y = x^3")
plt.legend()
plt.title("do thi ham so")
plt.show()