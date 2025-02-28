import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    x1=math.atan(x)
    x2=2*x*math.sin(x)
    x3=1.1958
    return x1+x2-x3
    
def grad_f(x):
    x1=1/(x*x+1)
    x2=2*(math.sin(x)+ x * math.cos(x))
    return x1+x2
 
def lap_f(x):
    x1=-2*x/(1+x*x)/(1+x*x)
    x2=2*(2*math.cos(x)-x*math.sin(x))
    return x1+x2

x_range=[-55,-40,-30,-20,-8,0,10,22,30,40,50]
for x in x_range:
    print("{:3}".format(x),end=' | ')
    x0=x
    iter=0  
    while (abs(f(x0))>1e-9) and (iter<1e4):
        x0-=f(x0)/grad_f(x0)
        iter=iter+1
        #print(f(x0),iter)
    
    print("{:6}".format(iter),' | ',"{:.6e}".format(x0),end=' | ')  
      
    x0=x
    iter=0  
    while (abs(f(x0))>1e-9) and (iter<1e4):
        x0-=2*f(x0)*grad_f(x0)/(2*grad_f(x0)*grad_f(x0)-f(x0)*lap_f(x0))
        #print(x0)
        #print(f(x0),'\n')
        iter=iter+1
    
    print("{:6}".format(iter),' | ',"{:.6e}".format(x0)) 
    
x=np.arange(-60,60,0.1)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.plot(x,[f(j) for j in x])
plt.show()