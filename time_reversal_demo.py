import numpy as np
import matplotlib.pyplot as plt


x = np.array([1, 2, 4, 5, 6, 9, 12])   # this is the signal
n = np.array([-2, -1, 0, 1, 2, 3, 4])  # this is the discrete time-axis

#  x[::-1] reverses the array
x_reversed = x[::-1]            # this is the time-reveresed signal
n_reversed = -n[::-1]           # this is the reversed time axis

plt.plot(n, x, '.-', c = 'b', label='orginal signal', alpha=0.6)
plt.plot(n_reversed, x_reversed, '.-', c='red', label='time reversed signal', alpha=0.6)
plt.title('Demo of time reversal of signal x[-n]')
plt.legend()
plt.grid(True)