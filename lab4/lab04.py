import numpy as np

def hilbert_matrix(n):
    H = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            H[i, j] = 1.0 / (i + j + 1)
    return H

def jacobi(A, b, x0=None, tol=5*1e-4, max_iterations=500000):
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    
    x = np.copy(x0)
    
    for iteration in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            sum_ax = np.dot(A[i], x) - A[i, i] * x[i]
            x_new[i] = (b[i] - sum_ax) / A[i, i]
        
        if np.linalg.norm(x_new - x, ord=1) < tol:
            return x_new, iteration + 1
        
        x = x_new
    
    return x, max_iterations

def gauss_seidel(A, b, x0=None, tol=5*1e-4, max_iterations=500000):
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    
    x = np.copy(x0)
    
    for iteration in range(max_iterations):
        x_new = np.copy(x)
        for i in range(n):
            sum_ax=0
            for j in range(n):
                if j<i:
                    sum_ax+=A[i][j]*x_new[j]
                elif j>i:
                    sum_ax+=A[i][j]*x[j]
            x_new[i] = (b[i] - sum_ax) / A[i, i]
        
        if np.linalg.norm(x_new - x, ord=1) < tol:
            return x_new, iteration + 1
        
        x = x_new
    
    return x, max_iterations

def steepest_descent(A, b, x0=None, tol=5*1e-4, max_iterations=500000):
    n = len(b)
    if x0 is None:
        x0 = np.zeros(n)
    
    x = np.copy(x0)
    
    for iteration in range(max_iterations):
        r = b - A @ x  
        alpha = np.dot(r, r) / np.dot(r, A @ r)  
        
        x += alpha * r  # 更新解
        
        if np.linalg.norm(alpha*r, ord=1) < tol:
            return x, iteration + 1
    
    return x, max_iterations


n = 800
H = hilbert_matrix(n)

x=np.ones(n)
x.reshape(n,1)
b=H@x

x_jacobi, iterations_jacobi = jacobi(H, b)
x_gauss, iterations_gauss = gauss_seidel(H, b)
x_sd, iterations_sd = steepest_descent(H, b)
#print("Jacobi:", x_jacobi)
print("iter:", iterations_jacobi)
print("wucha",np.linalg.norm(x_jacobi-x, ord=1))
#print("Gauss_seidel:", x_gauss)
print("iter:", iterations_gauss)
print("wucha",np.linalg.norm(x_gauss-x, ord=1))
#print("steepest_descent:", x_sd)
print("iter:", iterations_sd)
print("wucha",np.linalg.norm(x_sd-x, ord=1))


