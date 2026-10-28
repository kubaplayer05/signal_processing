# Fourier series
import numpy as np
import matplotlib.pyplot as plt

T0 = 1
cases = [0.25, 0.1]  # T1 values
k = np.arange(-15, 16)

def x(t, T0, T1):
    tm = (t + T0/2) % T0 - T0/2  # wrap t into one period [-T0/2, T0/2)
    return np.where(np.abs(tm) < T1, 1.0, 0.0)

def a(k, T0, T1):
    w0 = 2 * np.pi / T0
    ak = np.zeros(len(k))
    nz = k != 0
    ak[nz] = np.sin(k[nz] * w0 * T1) / (k[nz] * np.pi)
    ak[~nz] = 2 * T1 / T0
    return ak

t = np.linspace(-0.5, 0.5, 3001)

fig, axes = plt.subplots(2, 2, figsize=(10, 6))

for col, T1 in enumerate(cases):
    ax1, ax2 = axes[0, col], axes[1, col]

    ax1.plot(t, x(t, T0, T1), 'b')
    ax1.set_title(f'T0={T0}, T1={T1}')
    ax1.set_xlabel('t (s)')
    ax1.set_ylabel('x(t)')
    ax1.grid(True)

    ax2.stem(k, a(k, T0, T1), 'b', basefmt='k')
    ax2.set_xlabel('k')
    ax2.set_ylabel('a_k')
    ax2.grid(True)

fig.tight_layout()
fig.savefig("plot.png")