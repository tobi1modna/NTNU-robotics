import numpy as np
from rotations.rotations import rotz, rotx, roty
np.set_printoptions(suppress=True, precision=3)

a = np.array([[0.0, 0.0, 2/np.sqrt(5)],[0.0, 0.0, -1/np.sqrt(5)],[-2/np.sqrt(5), 1/np.sqrt(5), 0.0]])
R = np.eye(3) + np.sin(np.sqrt(5))*a + (1 - np.cos(np.sqrt(5)))*(a@a)

print(R)
print(np.sqrt(5))

p = np.array([1/np.sqrt(3), -1/np.sqrt(6), 1/np.sqrt(2)])
pp = rotz(np.deg2rad(-120)) @ roty(np.deg2rad(135)) @ rotx(np.deg2rad(30)) @ p.T
print(pp)
R = rotz(np.deg2rad(-120)) @ roty(np.deg2rad(135)) @ rotx(np.deg2rad(30))
print(R)

A = np.array([[np.sqrt(2), 1.0, 0],[0, 1.0, 2*np.sqrt(2)],[2.0, -1.0, 0]])
Ainv = np.linalg.inv(A)
B = np.array([[0, 1/np.sqrt(2), -np.sqrt(2)],[2.0, 1/np.sqrt(2), np.sqrt(2)],[np.sqrt(2), -np.sqrt(2), -2.0]])
R = B@Ainv

print(R)
print(1/np.sqrt(2))

Rab = rotx(np.deg2rad(30)) @ rotz(np.deg2rad(45))
print(Rab)