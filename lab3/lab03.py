import numpy as np
from scipy.linalg import solve_triangular

def hilbert_matrix(n):
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1.0 / (i + j + 1)
    return H

def doolittle_lu(A):
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))
    
    for i in range(n):
        # U 的第 i 行
        for k in range(i, n):
            U[i, k] = A[i, k] - sum(L[i, j] * U[j, k] for j in range(i))
        
        # L 的第 i 列
        for k in range(i + 1, n):
            L[k, i] = (A[k, i] - sum(L[k, j] * U[j, i] for j in range(i))) / U[i, i]
    
    return L, U

import numpy as np

def cholesky(A):
    n = A.shape[0]
    L = np.zeros_like(A)
    
    for i in range(n):
        for j in range(i + 1):
            if i == j:
                # 计算对角线元素
                L[i, j] = np.sqrt(A[i, i] - np.sum(L[i, :i] ** 2))
            else:
                # 计算非对角线元素
                L[i, j] = (A[i, j] - np.sum(L[i, :j] * L[j, :j])) / L[j, j]
    
    return L

def lu_solve(H, b):
    L, U = doolittle_lu(H)
    # 解 Ly = b (先解下三角方程)
    y = solve_triangular(L,  b, lower=True)
    # 解 Ux = y (再解上三角方程)
    x = solve_triangular(U, y)
    return x

def cholesky_solve(H, b):
    # 进行 Cholesky 分解
    L = cholesky(H)
    # 解 Ly = b (先解下三角方程)
    y = solve_triangular(L, b, lower=True)
    # 解 L^Tx = y (再解上三角方程)
    x = solve_triangular(L.T, y)
    return x

n = 19
H = hilbert_matrix(n)
#H=np.ones([n,n])

epsilon = 1e-16  # 给矩阵加上一个很小的正数确保正定
H_reg = H + epsilon * np.eye(n)

x=np.ones(n)
x.reshape(n,1)

b=H@x

x_lu=lu_solve(H,b)
x_cholesky=cholesky_solve(H_reg,b)

print(x)
print(x_lu)
print(doolittle_lu(H_reg))
print(np.linalg.norm(x_lu-x,1))
print(x_cholesky)
print(np.linalg.norm(x_cholesky-x,1))




'''
from scipy.linalg import lu

P, L1, U1 = lu(H)

print("P =\n", P)
print("L =\n", L1)
print(L)
print("U =\n", U1)
print(U)'''