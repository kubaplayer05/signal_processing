# Damped sinusoidal signal
import numpy as np
import matplotlib.pyplot as plt

a = -0.01
C = 1
omega = 1
fi = 0

t = np.linspace(-100, 100, num=1000)
x = C * np.exp(a * t) * np.cos(omega * t + fi)
f = C * np.exp(a * t)

plt.plot(t, x, 'b.-', t, f, 'r.-')
plt.xlabel('t(s)')
plt.ylabel('x(t)')
plt.title('x(t)=C*exp(at)*cos(Ωt+φ)')
plt.legend(['x(t)=C*exp(at)*cos(Ωt+φ)', 'f(t)=C*exp(at)'])
plt.grid(True)

plt.savefig("plot.png")