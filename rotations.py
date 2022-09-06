# File name: rotations.py
# Description: TPK4170, Example of rotations package  
# Author: Tobia Poppi
# Date: 06-09-2022

import numpy as np
np.set_printoptions(suppress=True)

def rotx(theta):
    ct = np.cos(theta)
    st = np.sin(theta)
    return np.array([[1.0, 0.0, 0.0],
                     [0.0, ct, -st],
                     [0.0, st, ct]])

def roty(theta):
    ct = np.cos(theta)
    st = np.sin(theta)
    return np.array([[ct, 0.0, st],
                     [0.0, 1.0, 0.0],
                     [-st, 0.0, ct]])

def rotz(theta):
    ct = np.cos(theta)
    st = np.sin(theta)
    return np.array([[ct, -st, 0.0],
                     [st, ct, 0.0],
                     [0.0, 0.0, 1.0]])

def vector(x):
    return np.array(x)


def main():
    #create a vector
    l = [1.0, 2.0, 3.0]
    v = vector(l)
    print(v)

    #create a rotation matrix
    theta = np.deg2rad(45)
    Rx = rotx(theta)
    print(Rx)

    #is this matrix a legit rotation matrix?
    #if yes, it should be (R transposed R) = I and det(R) = 1
    print(Rx.T @ Rx)
    
    #if determinant = -1 the matrix is a REFLECTION if it's = 1 it's a ROTATION
    print(np.linalg.det(Rx))


if __name__ == '__main__':
    main()
