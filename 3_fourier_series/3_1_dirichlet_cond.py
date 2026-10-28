# Signals violating Dirichlet conditions
import numpy as np
import matplotlib.pyplot as plt

T0 = 1

def wrap(t):
    return T0 - (-t) % T0  # map t into one period (0, T0]

def x1(t):
    return 1 / wrap(t)

def x2(t):
    return np.sin(2 * np.pi / wrap(t))

def x3(t):
    tm = t % T0  # [0, T0)
    # section n covers [1 - 2^-n, 1 - 2^-(n+1)) and has height 2^-n
    return 2.0 ** np.ceil(np.log2(1 - tm))

t = np.linspace(0, T0, 100001)[1:-1]  # one period, skip both ends

fig, axes = plt.subplots(3, 1, figsize=(8, 7))

for ax, x, title in zip(axes, [x1, x2, x3], ['Condition 1: x(t)=1/t',
                                             'Condition 2: x(t)=sin(2π/t)',
                                             'Condition 3: infinite number of sections']):
    ax.plot(t, x(t), 'b')
    ax.set_title(title)
    ax.set_xlabel('t (s)')
    ax.set_ylabel('x(t)')
    ax.grid(True)

axes[0].set_ylim(0, 10)

fig.tight_layout()
fig.savefig("plot.png")