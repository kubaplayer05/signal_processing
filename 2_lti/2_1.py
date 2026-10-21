# Numerical integration
import numpy as np
import matplotlib.pyplot as plt

exact_value = 10 / 3
N = 2
dt = 1 / N

def x(t):
    return -t**2 + 0.5 * t + 2

def rectangle_approximation(N):
    dt = 1 / N
    t = np.arange(-N, N) * dt

    return np.sum(x(t)) * dt

def trapezoid_approximation(N):
    dt = 1 / N
    t = np.arange(-N, N + 1) * dt
    heights = x(t)

    return np.sum((heights[:-1] + heights[1:]) / 2) * dt

I_rect = rectangle_approximation(N)
I_trap = trapezoid_approximation(N)

t_r = np.arange(-N, N) * dt          
t_t = np.arange(-N, N + 1) * dt      
tt = np.linspace(-1, 1, 100)

fig, (ax1, ax2) = plt.subplots(2, 1)

# rectangle approximation
ax1.plot(tt, x(tt), 'r')
ax1.step(np.append(t_r, t_r[-1] + dt), np.append(x(t_r), x(t_r)[-1]), 'b', where='post')
ax1.plot(t_r, x(t_r), 'b.')
ax1.set_title(f'Rectangle, N={N}, dt={dt} (s)')
ax1.set_ylim(0, 2.05)
ax1.set_xlabel('t(s)')
ax1.set_ylabel('x(t)')
ax1.grid(True)

# trapezoid approximation
ax2.plot(tt, x(tt), 'r')
ax2.plot(t_t, x(t_t), 'b.-')
ax2.set_title(f'Trapezoid, N={N}, dt={dt} (s)')
ax2.set_ylim(0, 2.05)
ax2.set_xlabel('t(s)')
ax2.set_ylabel('x(t)')
ax2.grid(True)

fig.tight_layout()
fig.savefig("plot.png")
