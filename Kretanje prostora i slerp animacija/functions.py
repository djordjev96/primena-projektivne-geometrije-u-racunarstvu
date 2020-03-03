import numpy as np
import math
import sys

def Euler2A(fi, teta, psi):
    Rx = np.array([[1, 0, 0],
                   [0, np.cos(fi), -np.sin(fi)],
                   [0, np.sin(fi), np.cos(fi)]])
    
    Ry = np.array([[np.cos(teta), 0, np.sin(teta)],
                   [0, 1, 0],
                   [-np.sin(teta), 0, np.cos(teta)]])
            
    Rz = np.array([[np.cos(psi), -np.sin(psi), 0],
                   [np.sin(psi), np.cos(psi), 0],
                   [0, 0, 1]])
    return np.dot(Rz, np.dot(Ry, Rx))


def AxisAngle(A):
    A_ = np.array(A - np.eye(3))

    # print(A_)
    # print(A_[1])

    p = np.cross(A_[1], A_[2]) / np.linalg.norm(np.cross(A_[1], A_[2]))
    if not (np.isclose(p[0],0) or np.isclose(p[1],0) or np.isclose(p[2],0)):
        p = np.cross(A_[0], A_[1]) / np.linalg.norm(np.cross(A_[0], A_[1]))
    else:
        p = np.cross(A_[1], A_[2]) / np.linalg.norm(np.cross(A_[1], A_[2]))


        # p = np.cross(A_[0], A_[1]) / np.linalg.norm(np.cross(A_[0], A_[1]))

    u = A_[1]
    up = np.matmul(A, u)
    fi = np.arccos(np.dot(u, up) / (np.linalg.norm(u) * np.linalg.norm(up)))

    if np.linalg.det(np.vstack((u,up,p))) < 0:
        p = -p

    return p, fi

def Rodrigez(p, fi):

    if not unitary(p):
        p = p / len(p)
    E = [[1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]]
    px = np.array([[0, -p[2], p[1]],
                   [p[2], 0, -p[0]],
                   [-p[1], p[0], 0]])
    
    p = np.matrix(p.reshape(3, 1))

    ppt = np.dot(p, np.transpose(p))

    return ppt + np.cos(fi)*(E - ppt) + np.sin(fi)*px

def A2Euler(A):
    fi = 0
    teta = 0
    psi = 0


    if(A[2,0] < 1):
        if(A[2,0] > -1):
            fi = np.arctan2(A[1,0], A[0,0])
            teta = np.arcsin(-A[2,0])
            psi = np.arctan2(A[2,1], A[2,2])
        else:
            fi = np.arctan2(-A[0,1], A[1,1])
            teta = np.pi/2
            psi = 0
    else:
        fi = np.arctan2(-A[0,1], A[1,1])
        teta = -np.pi/2
        psi = 0
    
    return fi, teta, psi

def AxisAngle2Q(p, fi):
    w = np.cos(fi/2)
    p = p / np.linalg.norm(p)

    x = np.sin(fi/2) * p[0]
    y = np.sin(fi/2) * p[1]    
    z = np.sin(fi/2) * p[2]

    if fi == 0:
        return np.array([1,0,0,0])
    else:
        return np.array([x,y,z,w])    

def Q2AxisAngle(q):    
    q = q / np.linalg.norm(q)
    if (q[3] < 0):
        q = -q
    fi = 2*np.arccos(q[3])
    
    p = [q[0], q[1], q[2]]

    if (np.abs(q[3]) == 1):
        p = [1,0,0]
    else:
        p = p / np.linalg.norm(p)

    return p, fi

def unitary(vector):
    return np.isclose(np.linalg.norm(vector), 1)

def Slerp(q1,q2,tm,t):
    if t == 0:
        return q1
    elif t == tm:
        return q2

    
    cos0 = np.dot(q1,q2) / (np.linalg.norm(q1) * np.linalg.norm(q2))

    if cos0 < 0: # idi po kracem luku sfere
        q1 = -q1
        cos0 = -cos0
    elif cos0 > 0.95: # q1 i q2 previse blizu
        return q1

    fi0 = np.arccos(cos0)

    qs = (np.sin(fi0*(1-t/tm))/np.sin(fi0)) * np.array(q1) + (np.sin(fi0*t/tm)/np.sin(fi0)) * np.array(q2) 
    
    return qs

# def main():
#     # A = Euler2A(-np.arctan(1/4), -np.arcsin(8/9), np.arctan(4))

#     # A = Euler2A(np.arcsin(np.sqrt(6)/4), np.arctan2(1,3), np.arctan2(np.sqrt(6), 2))



#     # print("Euler2A(arctan(1/4), -arcsin(8/9), arctan(4):")
#     # print(A)

#     A = np.array([
#         [3/4,1/4, np.sqrt(6)/4],
#         [1/4, 3/4, -np.sqrt(6)/4],
#         [-np.sqrt(6)/4, np.sqrt(6)/4, 2/4]
#     ])


#     # A = np.array([
#     #     [0, 0, 1],
#     #     [1, 0, 0],
#     #     [0, 1, 0]
#     # ])

#     A = np.array([
#          [0, 0, -1],
#          [0, -1, 0],
#          [-1, 0, 0]
#      ])

#     # p = np.array([0,3,0])
#     # fi = np.pi/4

#     print("AxisAngle(A)")
#     p, fi = AxisAngle(A)
#     print(p, fi)

#     print("Rodrigez(p, fi):")
#     Rp_fi = Rodrigez(p, fi)
#     print(Rp_fi)

#     print("A2Euler(A):")
#     A = Rp_fi
#     fi_, teta, psi = A2Euler(A)
#     print("fi, teta, psi = ", fi_, teta, psi)

#     print("AxisAngle2Q(p,fi):")
#     q = AxisAngle2Q(p,fi)
#     print(q)

#     print("Q2AxisAngle(q):")
#     p, fi = Q2AxisAngle(q)
#     print(p, fi)





if __name__ == '__main__':
    main()