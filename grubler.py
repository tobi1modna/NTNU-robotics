# File name: grubler.py
# Description: TPK4170, Solution of "problem 4" of 1st Assignment  
# Author: Tobia Poppi
# Date: 30-08-2022

def grubler(dof_rbody, n_links, joints, joints_dof):
    out_dof = dof_rbody*(int(n_links) - 1 - int(joints))+int(sum(joints_dof))
    return out_dof

def main():
    m = 3
    N = 4
    J = 4
    joints_dof = [1, 1, 1, 1]
    dof = grubler(m, N, J, joints_dof)
    print(dof)

if __name__ == "__main__":
    main()