# File name: rotations_example.py
# Description: TPK4170, Example of rotations package  
# Author: Tobia Poppi
# Date: 06-09-2022

from rotations.rotations import rotx, vector
import numpy as np



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


if __name__ == '__main__':
    main()