# Sinusoidal signal
import numpy as np
import matplotlib.pyplot as plt

A = 1
omega = 1
fi = 0

t = np.linspace(0, 10, num=100)
x = A * np.cos(omega * t + fi)
f = A/2 * np.exp(1j * fi) * np.exp(1j * omega * t) + A/2 * np.exp(-1j * fi) * np.exp(-1j * omega * t)

# should be nearly equal to zero, cuz both x and f are the same signal, just expressed differently
d = f - x

plt.plot(t, d)
plt.xlabel('t(s)')
plt.ylabel('x(t)')
plt.grid(True)

plt.savefig("plot.png")