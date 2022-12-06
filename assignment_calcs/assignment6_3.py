from this import s
import numpy as np
from modern_robotics import IKinSpace

if __name__ == "__main__":

    l1 = 0.425
    l2 = 0.392
    h1 = 0.160
    h2 = 0.09475
    w1 = 0.134
    w2 = 0.0815

    M = np.array([
      [-1, 0, 0, l1 + l2],
      [0, 0, 1, w1 + w2],
      [0, 1, 0, h1 - h2],
      [0, 0, 0, 1]
    ])

    S = np.array([
      [0,0,1,0,0,0],
      [0,1,0,-h1,0,0],
      [0,1,0,-h1, 0,l1],
      [0,1,0, -h1, 0, l1+l2],
      [0,0,-1, -w1, l1+l2, 0],
      [0,1,0, h2-h1, 0, l1+l2]
    ]).T

    T = np.array([[0, 1, 0, -0.5], [0, 0, -1, 0.1], [-1, 0, 0, 0.1], [0, 0, 0, 1]])
    th0 = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    
    th = IKinSpace(Slist=S, M=M, T=T, thetalist0=th0, eomg=0.001, ev=0.0001)
    print(th[0])
