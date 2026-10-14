# Exponential signal
import numpy as np
import matplotlib.pyplot as plt

a = -0.01
C = 1e4
Tmax = 100

t = np.linspace(-Tmax, Tmax, num=2*Tmax + 1)
x = C * np.exp(a * t)

plt.plot(t, x.real, 'b.-', t, x.imag, 'r.-')
plt.legend(['Re{x(t)}=cos(Ωt)', 'Im{x(t)}=sin(Ωt)'])
plt.xlabel('t(s)')
plt.ylabel('x(t)')
plt.title('x(t)=C*exp(at)')
plt.grid(True)

plt.savefig("plot.png")