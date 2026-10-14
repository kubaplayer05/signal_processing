# Complex exponential signal
import numpy as np
import matplotlib.pyplot as plt

omega = 1
t = np.linspace(0, 10, num=100)

x = np.exp(1j * omega * t)

plt.plot(t, x.real, 'b.-', t, x.imag, 'r.-')
plt.xlabel('t(s)')
plt.ylabel('x(t)')
plt.title('x(t)=exp(jΩt)')
plt.legend(['Re{x(t)}=cos(Ωt)', 'Im{x(t)}=sin(Ωt)'])
plt.grid(True)

plt.savefig("plot.png")