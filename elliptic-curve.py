import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-7, 7, 1000)

y_pos = np.sqrt(x**3 + 7)
y_neg = -np.sqrt(x**3 + 7)

fig, ax = plt.subplots()

ax.plot(x, y_pos, color="blue", label="Curva Eliptica secp256k1")
ax.plot(x, y_neg, color="blue")

ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.grid(color="grey", linestyle='-.', linewidth=0.5)

plt.ylim(-8, 8)
plt.xlim(-8, 8)

ax.plot([-8, 8], [0, 0], color='k', linestyle='-', linewidth=1.5)
ax.plot([0, 0], [-8, 8], color='k', linestyle='-', linewidth=1.5)

plt.show()
