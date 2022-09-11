# File name: rotations.py
# Description: TPK4170, Example of rotations package  
# Author: Tobia Poppi
# Date: 06-09-2022

import numpy as np
np.set_printoptions(suppress=True)


def vector(x, y, z):
    return np.array([[x], [y], [z]])

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


def angle_axis(omega, theta):
    #extract omega components
    wx, wy, wz = omega
    m_omega = np.array([[0.0, -wz, wy],[wz, 0.0, -wx],[-wy, wx, 0.0]])
    R = np.eye(3) + np.sin(theta) * m_omega + (1.0 - np.cos(theta)) * (m_omega @ m_omega)
    return R

