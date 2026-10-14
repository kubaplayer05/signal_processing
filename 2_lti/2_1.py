# Numerical integration
import numpy as np
import matplotlib.pyplot as plt

exact_value = 10 / 3
N = 2
t = np.linspace(-1, 1, 2*N+1)

def x(t):
    return -t**2 + 0.5 * t + 2

def rectangle_approximation(N, t):
    dt = 1 / N
    n = np.arange(-N, N)
    t = n * dt

    return np.sum(x(t)) * dt

I_rect = rectangle_approximation(N, t)

plt.plot(t, I_rect, "b.-")
plt.xlabel('t(s)')
plt.ylabel('x(t)')
plt.grid(True)

plt.savefig("plot.png")


