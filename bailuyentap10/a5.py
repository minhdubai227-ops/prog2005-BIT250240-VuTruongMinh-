import matplotlib.pyplot as plt
import numpy as np
fig, (ax1, ax2) = plt.subplots(1, 2)
x = np.linspace(0, 10, 100)
ax1.plot(x, x**2)
ax1.set_title("y = x^2")
ax2.plot(x, np.sqrt(x))
ax2.set_title("y = sqrt(x)")
plt.show()