# Convolution integral
import numpy as np
import matplotlib.pyplot as plt

tx = np.linspace(-2, 2, 100)
ty = np.linspace(-4, 4, 100)

def x(t):
    return np.where(np.abs(t) < 1, 0.5, 0)

def h(t):
    return np.where(np.abs(t) < 1, t + 1, 0)

tau = np.linspace(-3, 3, 2001)
y = np.array([np.trapezoid(x(tau) * h(ti - tau), tau) for ti in ty])

plt.plot(ty, y, 'b')
plt.xlabel('t(s)')
plt.ylabel('y(t)')
plt.title('y(t)=x(t)*h(t)')
plt.grid(True)

plt.savefig("plot.png")