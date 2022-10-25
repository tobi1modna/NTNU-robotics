import numpy as np
from modern_robotics import FKinBody, FKinSpace

from sympy import symbols, cos, sin, Matrix, diag, zeros, eye
from sympy.physics.mechanics import dynamicsymbols, mechanics_printing
mechanics_printing()

#problem 1 - b

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

th1, th2, th3, th4 = dynamicsymbols("theta_1, theta_2, theta_3, theta_4")
L1, L2, L3, L4 = symbols("L_1, L_2, L_3, L_4")


S1 = Matrix([[0],[0],[1],[0],[-L1],[0]])
S2 = Matrix([[0],[0],[1],[0],[-L1-L2],[0]])
S3 = Matrix([[0],[0],[1],[0],[-L1-L2-L3],[0]])
S4 = Matrix([[0],[0],[1],[0],[-L1-L2-L3-L4],[0]])

B1 = Matrix([[0],[0],[1],[0],[L1+L2+L3+L4],[0]])
B2 = Matrix([[0],[0],[1],[0],[L2+L3+L4],[0]])
B3 = Matrix([[0],[0],[1],[0],[L3+L4],[0]])
B4 = Matrix([[0],[0],[1],[0],[L4],[0]])


Js1 = S1
Js2 = Ad(exp6(S1, th1)) * S2
Js3 = Ad(exp6(S1, th1) * exp6(S2, th2)) * S3
Js4 = Ad(exp6(S1, th1) * exp6(S2, th2) * exp6(S3, th3)) * S4


Jb4 = B4
Jb3 = Ad(exp6(B4, th4)) * B3
Jb2 = Ad(exp6(B4, th4) * exp6(B3, th3)) * B2
Jb1 = Ad(exp6(B4, th4) * exp6(B3, th3) * exp6(B2, th2)) * B1
Jb3.simplify()
Jb2.simplify()
Jb4.simplify()
print(Jb1)
print(Jb2)
print(Jb3)
print(Jb4)

a = np.array([[0, 1/np.sqrt(2), 0], [-1/np.sqrt(2), 0, 1/np.sqrt(2)], [0, -1/np.sqrt(2), 0]])
print(a@a)
