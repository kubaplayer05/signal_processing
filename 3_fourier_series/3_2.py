# Fourier integral
import numpy as np
import matplotlib.pyplot as plt

A = 1
phi = 0
W0 = 50     # carrier (rad/s)
Wm = 15     # modulating (rad/s)
k_AM = 0.5

t = np.linspace(-1, 1, 4001)  # signals are zero outside |t| < 1
W = np.linspace(-100, 100, 2001)

x1 = np.ones(len(t))
x2 = A * np.cos(W0 * t + phi)
x3 = (1 + k_AM * np.cos(Wm * t)) * np.cos(W0 * t + phi)

def fourier(x):
    return np.array([np.trapezoid(x * np.exp(-1j * w * t), t) for w in W])

signals = [(x1, 'Rectangular impulse'),
           (x2, f'Ω0={W0} (rad/s)'),
           (x3, f'Ω0={W0} (rad/s), Ωm={Wm} (rad/s), k_AM={k_AM}')]

fig, axes = plt.subplots(3, 2, figsize=(12, 8))

for (ax1, ax2), (x, title) in zip(axes, signals):
    ax1.plot(t, x, 'b')
    ax1.set_title(title)
    ax1.set_xlabel('t (s)')
    ax1.set_ylabel('x(t)')
    ax1.grid(True)

    ax2.plot(W, np.abs(fourier(x)), 'b')
    ax2.set_xlabel('Ω (rad/s)')
    ax2.set_ylabel('|X(Ω)|')
    ax2.grid(True)

axes[0, 0].set_ylim(0, 2)

fig.tight_layout()
fig.savefig("plot.png")