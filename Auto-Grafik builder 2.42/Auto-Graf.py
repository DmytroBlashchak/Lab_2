import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

x = [160, 320, 640, 960, 1280, 1600, 3200, 6400, 9600, 12800, 16000]
y = [-1.01, -1.2, -1.72, -1.93, -2.38, -3.1, -6.7, -12.3, -15.9, -20, -21.3, ] 

plt.figure(figsize=(14, 5))

f = interp1d(x, y, kind='linear')

x_smooth = np.array(x)
y_smooth = f(x_smooth)

plt.plot(x_smooth, y_smooth, 'bo-', markersize=4)

plt.xscale('log')
plt.xlabel('')
plt.ylabel('')
plt.title('')
plt.grid(True)

ax = plt.gca()
ax.set_xscale('log')
ax.set_xticks(x)
ax.set_xticklabels(x)

y_ticks = np.arange(0, -22, -3)
y_tick_labels = ['{:g}'.format(y) for y in y_ticks] 
plt.yticks(y_ticks, y_tick_labels)

x_text = x[-1] * 1.275
y_text = min(y_smooth) - 1.5
plt.text(x_text, y_text, '', ha='center', va='top')

x_text_y = x[-11] / 1.1
y_text_y = max(y_smooth) + 2
plt.text(x_text_y, y_text_y, '', ha='right', va='bottom')

plt.show() 
