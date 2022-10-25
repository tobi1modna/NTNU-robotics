import numpy as np
from modern_robotics import FKinBody, FKinSpace

#problem 2

L0 = 1
L1 = 1
L2 = 1

M = np.array([[1, 0, 0, 0],
              [0, 1, 0, L1+L2],
              [0, 0, 1, L0],
              [0, 0, 0, 1]])

thetalist = np.array([0, np.pi/2, -np.pi/2, 1])

Slist = np.array([[0, 0, 1, 0, 0, 0],
                  [0, 0, 1, L1, 0, 0],
                  [0, 0, 1, L1+L2, 0, 0],
                  [0, 0, 0, 0, 0, 1]]).T

Blist = np.array([[0, 0, 1, -L1-L2, 0, 0],
                  [0, 0, 1, -L2, 0, 0],
                  [0, 0, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 1]]).T

T_s = FKinSpace(M, Slist, thetalist)
T_b = FKinBody(M, Blist, thetalist)
print(np.array_equal(T_s, T_b))
print(T_s)

##problem 4

L1 = 425
L2 = 392
H1 = 89
H2 = 95
W1 = 109
W2 = 82

thetalist = np.array([0, -np.pi/2, -np.pi/2, 0, 0, 0])

M = np.array([[-1, 0, 0, L1+L2],
              [0, 0, 1, W1+W2],
              [0, 1, 0, H1-H2],
              [0, 0, 0, 1]])

Slist = np.array([[0, 0, 1, 0, 0, 0],
                  [0, 1, 0, -H1, 0, 0],
                  [0, 1, 0, -H1, 0, L1],
                  [0, 1, 0, -H1, 0, L1+L2],
                  [0, 0, -1, -W1, L1+L2, 0],
                  [0, 1, 0, H2-H1, 0, L1+L2]]).T

Blist = np.array([[0, 1, 0, W2+W1, 0, L2+L1],
                  [0, 0, 1, H2, -L2-L1, 0],
                  [0, 0, 1, H2, -L2, 0],
                  [0, 0, 1, H2, 0, 0],
                  [0, -1, 0, -W2, 0, 0],
                  [0, 0, 1, 0, 0, 0]]).T

T_s = np.round(FKinSpace(M, Slist, thetalist))
T_b = np.round(FKinBody(M, Blist, thetalist))
print(np.array_equal(T_s, T_b))
print(T_s)