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

start_point = (-1.8,1.2)
end_point = (2,4)
mid_point = (0.17, 2.65)
final_point = (2,-4)
text_point = (-4,-4)


#LINEAS
ax.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], 'r-', label='Línea recta')
ax.plot([end_point[0], end_point[0]], [-4, end_point[1]], 'r--', label='Línea recta discontinua')


#PUNTOS
ax.scatter([start_point[0], end_point[0]], [start_point[1], end_point[1]], color='red')
ax.scatter(mid_point[0], mid_point[1], color='red')
ax.scatter(final_point[0], final_point[1], color='red')


#LABELS
ax.annotate('A', start_point, textcoords="offset points", xytext=(0,10), ha='center')
ax.annotate('-C', end_point, textcoords="offset points", xytext=(0,10), ha='center')
ax.annotate('B', mid_point, textcoords="offset points", xytext=(0,10), ha='center')
ax.annotate('C', final_point, textcoords="offset points", xytext=(2,10), ha='left')
ax.annotate('A + B = C', text_point, textcoords="offset points", xytext=(2,10), ha='left', fontsize=14)


ax.grid(color="grey", linestyle='-.', linewidth=0.5)

 # Establecemos relación de aspecto

plt.ylim(-8, 8)
plt.xlim(-8, 8)

plt.show()
