import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100)
y = np.sin(x)
"""
plt.plot(x, y, color="red", linewidth=2, linestyle="--")
plt.scatter(x, y, color="blue", marker="o", s=5)
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.title("Sine Wave")
plt.grid(True)
plt.show()
"""
#      Subplots
fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(x, y, color="red", linestyle="-.")
axs[0, 1].scatter(x, y, color="magenta", marker="4")
axs[1, 0].bar(x, y, color="indigo")
axs[1, 1].hist(y, edgecolor="black", facecolor="blue")
axs[2, 0].boxplot(y)
axs[2, 1].pie(x, y)
# .contourf(x, y, z)
# .axes(projection='3d')
plt.show()

