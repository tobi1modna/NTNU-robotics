import numpy as np
from rotations.rotations import rotz, rotx, roty
np.set_printoptions(suppress=True, precision=3)

a = np.array([[0.0, 0.0, 2/np.sqrt(5)],[0.0, 0.0, -1/np.sqrt(5)],[-2/np.sqrt(5), 1/np.sqrt(5), 0.0]])
R = np.eye(3) + np.sin(np.sqrt(5))*a + (1 - np.cos(np.sqrt(5)))*(a@a)

i = np.eye(3)
w = np.array([[0.0, -1/np.sqrt(3), -1/np.sqrt(3)],[1/np.sqrt(3), 0.0, -1/np.sqrt(3)],[1/np.sqrt(3), 1/np.sqrt(3), 0.0]])
print(w)

theta = (2/3)*np.pi
G_inv = (1/theta)*i - (1/2)*w + ((1/theta) - ((1/2)*(1/np.tan(theta/2))))*(w@w)
print(G_inv)
print(G_inv@np.array([[3],[0],[0]]))
a = np.array([[1/np.sqrt(3)],[-1/np.sqrt(3)],[1/np.sqrt(3)]])
print(a)
b = np.array([-1, 1, 0])
print(b)
print(a*b)
#print(1/np.sqrt(3) * 0.827)
#print(1.055-0.477)
#print(-1.055+0.477)
#print(-0.677-0.477)
#print(-1.154/-0.577)
#print(1.154 + 0.477)
#print(1.154 - 0.477)
#print(1.154 + 0.477)
#print()

theta = np.sqrt(5)
a = np.array([[0.0, -2/np.sqrt(5), 1/np.sqrt(5)],[2/np.sqrt(5), 0.0, 0.0],[-1/np.sqrt(5), 0.0, 0.0]]) 

R = np.eye(3) + np.sin(np.sqrt(5))*a + (1 - np.cos(np.sqrt(5)))*(a@a)
print(R)

f = (np.eye(3)*theta + (1 - np.cos(theta))*a + (theta - np.sin(theta))*(a@a)) @ np.array([3/np.sqrt(5), 0, 0])
print(f)