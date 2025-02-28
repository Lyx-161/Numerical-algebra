import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    x=np.float32(x**2)
    x=np.float32(x+25)
    x=np.float32(math.sqrt(x))
    return np.float32(x-5)

def g(x):
    x2=np.float32(x**2)
    x=np.float32(x2+25)
    x=np.float32(math.sqrt(x))
    x=np.float32(x+5)
    return np.float32(x2/x)

print('{0:35s} {1:20s} {2:25s}'.format('  x','f(x)','g(x)'))

for i in range(1,12):
    x=4**(-i)
    f_val=f(x)
    g_val=g(x)
    x_val_formatted = "{:.12e}".format(np.float32(x))
    f_val_formatted = "{:.12e}".format(np.float32(f_val))
    g_val_formatted = "{:.12e}".format(np.float32(g_val))
    print('4^','{0:3d}'.format(-i),"="'{0:20s} {1:20s} {2:25s}'.format(x_val_formatted,f_val_formatted,g_val_formatted))

for i in range(1,12):
    x=4**(-i)
    cha=f(x)-g(x)
    x_val_formatted = "{:.12e}".format(np.float32(x))
    cha_val_formatted = "{:.12e}".format(np.float32(cha))
    print('4^','{0:3d}'.format(-i),"="'{0:20s} {1:20s}'.format(x_val_formatted,cha_val_formatted))

x=np.arange(0,0.2,0.0000001)
plt.plot(x,[f(j)-g(j) for j in x])

plt.show()