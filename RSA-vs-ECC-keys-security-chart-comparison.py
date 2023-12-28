import matplotlib.pyplot as plt

x = [96, 112, 128, 192, 256]
y = [192, 224, 256, 384, 521]
y2 = [1536, 2048, 3072, 7680, 15360]

plt.plot(x, y, label='ECC')
plt.plot(x, y2, label='RSA')

for i, txt in enumerate(y):
    plt.text(x[i], y[i], str(txt), ha='center', va='bottom', fontsize=8)

for i, txt in enumerate(y2):
    plt.text(x[i], y2[i], str(txt), ha='center', va='baseline', fontsize=8)

plt.xlabel('Bits Equivalentes')
plt.ylabel('Bits en ECC y RSA')
plt.title("Nivel de Seguridad Equivalente")
plt.legend()
plt.grid(True)

# Guardar la figura con mayor resolución (dpi=300)

plt.show()
