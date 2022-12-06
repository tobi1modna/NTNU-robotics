import numpy as np

L1 = 3 #Fixed Length of L1
L2 = 2 #Fixed Length of L2
L3 = 1 #Fixed Length of L3

if __name__ == "__main__":

    E = (4, 2) #Fixed coordinates of end-effector frame
    t = 0 #Fixed orientation of end-effector frame

    P = (E[0] - L3*np.cos(t), E[1] - L3*np.sin(t))
    alpha = np.arccos((L1**2 - L2**2 + P[0]**2 + P[1]**2)/(2*L1*np.sqrt(P[0]**2 + P[1]**2)))
    gamma = np.arctan2(P[1], P[0])
    beta = np.arccos((L1**2 + L2**2 - P[0]**2 - P[1]**2)/(2*L1*L2))

    th1_a = gamma - alpha
    th1_b = gamma + alpha
    th2_a = np.pi - beta
    th2_b = beta - np.pi
    th3_a = t - th2_a - th1_a
    th3_b = t - th2_b - th1_b

    solution_ed = (th1_a, th2_a, th3_a)
    solution_eu = (th1_b, th2_b, th3_b)

    print("Solution Elbow Down: " + str(solution_ed))
    print("Solution Elbow Up: " + str(solution_eu))