# Convolution splines
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-6, 6, 12001)
dt = t[1] - t[0]
k = int(round(1 / dt))

colors = ['r', 'lime', 'b', 'k']

b = np.where(np.abs(t) < 1, 1.0, 0.0)  # beta^0

for P in range(1, 5):
    # beta^P(t) = integral of beta^(P-1) over [t-1, t+1]
    F = np.concatenate(([0.0], np.cumsum((b[1:] + b[:-1]) / 2 * dt)))
    nb = np.zeros_like(b)
    nb[k:-k] = F[2*k:] - F[:-2*k]
    b = nb

    plt.plot(t, b, colors[P-1], label=fr'$\beta^{P}$')

plt.title(r'$\beta(t)^P=\beta(t)^0*\beta(t)^0*\ ...\ *\beta(t)^0$')
plt.xlim(-5, 5)
plt.ylim(0, 10)
plt.xlabel('t (s)')
plt.ylabel('y(t)')
plt.legend()
plt.grid(True)

plt.savefig("plot.png")
