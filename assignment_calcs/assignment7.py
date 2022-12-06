import numpy as np
from modern_robotics import FKinBody, FKinSpace

from sympy import symbols, cos, sin, Matrix, diag, zeros, eye
from sympy.physics.mechanics import dynamicsymbols, mechanics_printing
mechanics_printing()

def skew(v):
    return Matrix([[0, -v[2], v[1]],
                   [v[2], 0, -v[0]],
                   [-v[1], v[0], 0]])

def exp3(omega, theta):
    omega = skew(omega)
    R = eye(3) + sin(theta) * omega + (1 - cos(theta)) * omega * omega
    return R

def exp6(twist, theta):
    omega = skew(twist[:3])
    v = Matrix(twist[3:])
    T = eye(4)
    T[:3, :3] = exp3(twist[:3], theta)
    T[:3, 3] = (eye(3) * theta + (1 - cos(theta)) * omega +
                (theta - sin(theta)) * omega * omega) * v
    return T

def Ad(T):
    AdT = zeros(6)
    R = Matrix(T[:3, :3])
    AdT[:3, :3] = R
    AdT[3:, 3:] = R
    AdT[3:, :3] = skew(T[:3, 3]) * R
    return AdT

th1, th2, = dynamicsymbols("theta_1, theta_2")



a = np.array([0,0,6,0,6,0])

b = np.zeros((6,6))
b[1,1] = 4
b[2,2] = 4
b[3,3] = 2
b[4,4] = 2
b[5,5] = 2

print(a@b@a.T)

a = np.array([[11, np.sqrt(2)],
              [np.sqrt(2), 6]])

eigvals, eigvects = np.linalg.eig(a)
print(eigvals)
print(eigvects)

