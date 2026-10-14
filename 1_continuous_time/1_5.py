# Amplitude and Frequency modulation
import numpy as np
import matplotlib.pyplot as plt

omega_0 = 10
omega_m = 1
k_fm = 5

t = np.linspace(0, 10, num=1000)
x = np.cos(omega_0 * t + k_fm * np.cos(omega_m * t))
omega_inst = omega_0 - k_fm / omega_m * np.sin(omega_m * t)

fig, ax = plt.subplots()
ax.plot(t, x, 'b')
ax.set_xlabel('t(s)')
ax.set_ylabel('x(t)', color='b')
ax.tick_params(axis='y', colors='b')
ax.set_ylim(-1, 1)
ax.set_title('Ω0=10 (rad/s), Ωm=1 (rad/s), kFM=5')

ax2 = ax.twinx()
ax2.plot(t, omega_inst, 'r')
ax2.set_ylabel('Ωinst (rad/s)', color='r')
ax2.tick_params(axis='y', colors='r')
ax2.set_ylim(5, 15)

fig.savefig("plot.png")
