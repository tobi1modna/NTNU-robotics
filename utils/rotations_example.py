# File name: rotations_example.py
# Description: TPK4170, Example of rotations package  
# Author: Tobia Poppi
# Date: 06-09-2022

from rotations.rotations import rotx, rotz, vector, roty, angle_axis
import numpy as np
import modern_robotics as mr

np.set_printoptions(suppress=True)

def main():
    #create a rotation matrix
    theta = np.deg2rad(45)
    Rx = rotx(theta)
    print(Rx)

    #is this matrix a legit rotation matrix?
    #if yes, it should be (R transposed R) = I and det(R) = 1
    print(Rx.T @ Rx)
    
    #if determinant = -1 the matrix is a REFLECTION if it's = 1 it's a ROTATION
    print(np.linalg.det(Rx))


    #create a vector
    p = vector(1., 2., 3.)
    print(p)

    #rotate the vector
    q = Rx @ p
    #or
    q = Rx.dot(p)
    print(q)

    #rotation matrix of a 90deg rotation about z-axis of standard s frame.
    R = rotz(np.deg2rad(90))
    
    #random frame b
    Rsb = roty(np.random.rand())

    #rotation about z-axis of the base frame (s)
    print(R @ Rsb)

    #rotation about z-axis of the current frame (b)
    print(Rsb @ R)

    #rotation with axis-angle representation
    print(angle_axis(np.array([1, 0, 0]), np.deg2rad(30)))

    R2 = mr.MatrixExp3(mr.VecToso3([1.0, 0.0, 0.0]) * np.deg2rad(30))
    print(R2)

    logR2 = mr.AxisAng3(mr.so3ToVec(mr.MatrixLog3(R2)))
    print(logR2)

    axis, angle = logR2
    print(np.rad2deg(angle))

if __name__ == '__main__':
    main()