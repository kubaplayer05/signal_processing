import numpy as np
import matplotlib.pyplot as plt

T0 = 1
T1 = 0.25
w0 = 2 * np.pi / T0

def x(t):
    tm = (t + T0/2) % T0 - T0/2  # wrap t into one period [-T0/2, T0/2)
    return np.where(np.abs(tm) < T1, 1.0, 0.0)

def a(k):
    if k == 0:
        return 2 * T1 / T0
    return np.sin(k * w0 * T1) / (k * np.pi)

def x_N(t, N):
    xN = np.zeros(len(t), dtype=complex)
    for k in range(-N, N + 1):
        xN += a(k) * np.exp(1j * k * w0 * t)
    return xN.real  # imaginary part is ~0, because a_k = a_-k

def E(N):
    return np.trapezoid(np.abs(x(t) - x_N(t, N))**2, t)

t = np.linspace(-T0/2, T0/2, 4001)  # one period

# approximations for selected N
fig, axes = plt.subplots(2, 2, figsize=(10, 6))

for ax, N in zip(axes.T.flat, [1, 3, 5, 101]):
    ax.plot(t, x(t), 'b', t, x_N(t, N), 'k')
    ax.text(-0.1, 0.5, f'N={N}\nE_N={E(N):.2e}')
    ax.set_xlabel('t (s)')
    ax.set_ylabel('x(t)')
    ax.grid(True)

fig.tight_layout()
fig.savefig("plot.png")

# error as a function of N
Ns = np.arange(1, 100, 2)
errors = [E(N) for N in Ns]

plt.figure()
plt.stem(Ns, errors, linefmt='b-', markerfmt='b.', basefmt='k')
plt.xlim(0, 101)
plt.ylim(0, None)
plt.xlabel('N')
plt.ylabel('E_N')
plt.grid(True)

plt.savefig("error.png")