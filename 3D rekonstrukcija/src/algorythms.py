import numpy as np

# y^T F x = 0
# jed [{a1, a2, a3}, {b1, b2, b3}]= { a1b1, a2b1, a3b1, a1b2, a2b2, a3b2, a1b3,a2b3,a3b3};

def jed8(x,y):
    matrix = []
    for i in range(x.shape[0]):
        matrix.append(
            np.array([x[i][0] * y[i][0],
                      x[i][1] * y[i][0],
                      x[i][2] * y[i][0],
                      x[i][0] * y[i][1],
                      x[i][1] * y[i][1],
                      x[i][2] * y[i][1],
                      x[i][0] * y[i][2],
                      x[i][1] * y[i][2],
                      x[i][2] * y[i][2]
            ])
        )
    return np.array(matrix)   

def check_test(matrix,xx,yy):
    for i in range(8):
        if(np.isclose(np.dot(np.dot(np.transpose(yy[i]),matrix),xx[i]), 0)):
            continue
        else:
            print("Nije blizu nuli")

def check_det(matrix):
    return np.isclose(np.linalg.det(matrix), 0)

def get_affine_coord(x):
    x = (1/x[-1])*x
    return x

def triangulation(x, y, e, ff):
    T1 = np.eye(3,4)

    E2 = np.array([[0, -e[2], e[1]],
                  [e[2], 0, -e[0]],
                  [-e[1], e[0], 0]])

    T2 = np.transpose(np.vstack((np.transpose(E2 @ ff), e)))

    u, d, v = np.linalg.svd(get_equations(x, y, T1, T2))

    # v = -v

    # print(v[-1][:3])
    # print(v)
    # print(get_affine_coord(np.transpose(v[-1][:3])))

    # return 1/(np.transpose(v[-1])[-1])*np.transpose(v[-1])
    return get_affine_coord(np.transpose(v[-1])[:3])

def get_equations(x, y, T1, T2):
    return np.array([x[1]*T1[2] - x[2]*T1[1], -x[0]*T1[2] + x[2]*T1[0], 
                     y[1]*T2[2] - y[2]*T2[1], -y[0]*T2[2] + y[2]*T2[0]])


def get_ff_and_e(xx, yy):
    matrix = jed8(xx, yy)
    print("jed8 matrix:")
    print(matrix)

    U, D, V = np.linalg.svd(matrix)
    # D_ = np.zeros((8,9))
    # np.fill_diagonal(D_,D)

    print("u d v")
    print(U)
    print(D)
    print(V)

    Fvector = V[-1]

    print("Fvector")
    print(Fvector)

    FF = Fvector.reshape(3,3)

    print("Matrix FF")
    print(FF)

    ################ provere ############
    check_test(FF,xx,yy)
    check_det(FF)
    #####################################

    U1, D1, V1 = np.linalg.svd(FF)

    # print("U1, D1, V1")
    # print(-U1)
    # print(D1)
    # print(V1)

    # print(np.transpose(-V1))

    e1 = -V1[-1]
    e1 = get_affine_coord(e1)
    print("e1")
    print(e1)
    # F^T = (UDV^T)^T = VDU^T => VDU = svd(F.T)
    U1 = np.transpose(U1)
    e2 = -U1[-1]
    
    e2 = get_affine_coord(e2)
    print("e2")
    print(e2)

    DD1 = np.diag((1, 1, 0)) * D1

    print("DD1")
    print(DD1)
    
    FF1 = np.transpose(U1) @ DD1 @ V1

    print("FF1")
    print(FF1)

    FF_det = np.linalg.det(FF)
    FF1_det = np.linalg.det(FF1)

    print(FF_det)
    print(FF1_det)
    
    return FF1, e2