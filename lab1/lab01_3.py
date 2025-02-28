import numpy as np
import math

PI=3.1415926535897932

def compute_sin(u):
    fenzi=1-(29593/207636)*u**2+(34911/7613320)*u**4-(479249/11511339840)*u**6
    fenmu=1+(1671/69212)*u**2+(97/351384)*u**4+(2623/1644477120)*u**6
    return u*fenzi/fenmu

def jiecheng(x):
    sum=1
    for i in range(x):
        sum=sum*(i+1)
    return sum

def taylor_formular(x):
    return x-x**3/jiecheng(3)+x**5/jiecheng(5)-x**7/jiecheng(7)

print('{:.9s}'.format('PI/2024'),'\t','{:.9e}'.format(compute_sin(PI/2024)),'\t','{:.9e}'.format(taylor_formular(PI/2024)),'\t','{:.9e}'.format(taylor_formular(PI/2024)-compute_sin(PI/2024)),'\n')
print('{:.9s}'.format('PI/10'),'\t','{:.9e}'.format(compute_sin(PI/10)),'\t','{:.9e}'.format(taylor_formular(PI/10)),'\t','{:.9e}'.format(taylor_formular(PI/10)-compute_sin(PI/10)),'\n')
print('{:.9s}'.format('PI/6'),'\t','{:.9e}'.format(compute_sin(PI/6)),'\t','{:.9e}'.format(taylor_formular(PI/6)),'\t','{:.9e}'.format(taylor_formular(PI/6)-compute_sin(PI/6)),'\n')
print('{:.9s}'.format('PI/4'),'\t','{:.9e}'.format(compute_sin(PI/4)),'\t','{:.9e}'.format(taylor_formular(PI/4)),'\t','{:.9e}'.format(taylor_formular(PI/4)-compute_sin(PI/4)),'\n')
print('{:.9s}'.format('PI/3'),'\t','{:.9e}'.format(compute_sin(PI/3)),'\t','{:.9e}'.format(taylor_formular(PI/3)),'\t','{:.9e}'.format(taylor_formular(PI/3)-compute_sin(PI/3)),'\n')


print('{:.9s}'.format('PI/2024'),'\t','{:.9e}'.format(compute_sin(PI/2024)-math.sin(PI/2024)),'\t','{:.9e}'.format(taylor_formular(PI/2024)-math.sin(PI/2024)),'\n')
print('{:.9s}'.format('PI/10'),'\t','{:.9e}'.format(compute_sin(PI/10)-math.sin(PI/10)),'\t','{:.9e}'.format(taylor_formular(PI/10)-math.sin(PI/10)),'\n')
print('{:.9s}'.format('PI/6'),'\t','{:.9e}'.format(compute_sin(PI/6)-math.sin(PI/6)),'\t','{:.9e}'.format(taylor_formular(PI/6)-math.sin(PI/6)),'\n')
print('{:.9s}'.format('PI/4'),'\t','{:.9e}'.format(compute_sin(PI/4)-math.sin(PI/4)),'\t','{:.9e}'.format(taylor_formular(PI/4)-math.sin(PI/4)),'\n')
print('{:.9s}'.format('PI/3'),'\t','{:.9e}'.format(compute_sin(PI/3)-math.sin(PI/3)),'\t','{:.9e}'.format(taylor_formular(PI/3)-math.sin(PI/3)),'\n')