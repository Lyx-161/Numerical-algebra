import numpy as np
#Hilbert矩阵
def hilbert(n):
    H=np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            H[i][j]=1/(i+j+1)
    return H
#b
def find_b(H):
    n=H.shape[0]
    x_exact = np.ones(n)
    b=np.dot(H,x_exact)
    return b
#convergence threshold and maximum iterations
epsilon=5e-4
max=500000
#Jacobi
def Jacobi(H,b):
    n=H.shape[0]
    x=np.zeros(n)
    for i in range(max):
        u=np.copy(x)#这里需要用到copy函数只复制数值，不然会复制地址导致u和x完全相同，一起变动
        for j in range(n):
            #s=sum(H[j,t]*x[t] for t in range(n) if t!=j)
            s=H[j].dot(x)-H[j,j]*x[j]
            u[j]=(b[j]-s)/H[j][j]
        if np.linalg.norm(u-x,ord=1)<epsilon:
            return u,i+1
        x=u
    return x,max
#Gauss-Seidel
def Gauss(H,b):
    n=H.shape[0]
    x=np.zeros(n)
    for i in range(max):
        u=np.copy(x)
        for j in range(n):
            #s=sum(H[j,t]*u[t] for t in range(j) if t<j)#这里再回去看看Gauss的伪代码，你原来写的和jacobi没区别
            #s+=sum(H[j,t]*x[t] for t in range(j+1,n) if t>j)
            s=H[j].dot(u)-H[j,j]*u[j]
            u[j]=(b[j]-s)/H[j][j]
        if np.linalg.norm(u-x,ord=1)<epsilon:
            return u,i+1
        x=u
    return x,max
#SD
def SD(H,b):
    n=H.shape[0]
    x=np.zeros(n)
    for i in range(max):
        v=b-np.dot(H,x)
        t=np.dot(v,v)/np.dot(v,np.dot(H,v))
        u=x+t*v
        if np.linalg.norm(u-x,ord=1)<epsilon:
            return u,i+1
        x=u
    return x,max
#N=[10,50,100,200,800]
N=[10]
for i in range(len(N)):
    n=N[i]
    H=hilbert(n)
    x=np.ones(n)#这里误差计算应该是x_1-x，所以你的误差特别大，后面已经改过来了
    b=find_b(H)
    x1,max1=Jacobi(H,b)
    e1=np.linalg.norm(x1-x,ord=1)
    x2,max2=Gauss(H,b)
    e2=np.linalg.norm(x2-x,ord=1)
    x3,max3=SD(H,b)
    e3=np.linalg.norm(x3-x,ord=1)
    print(n)
    print(max1,e1)
    print(max2,e2)
    print(max3,e3)