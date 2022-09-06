# File name: rotations_example.py
# Description: TPK4170, Example of rotations package  
# Author: Tobia Poppi
# Date: 06-09-2022

from rotations import rotx, vector
import numpy as np



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
