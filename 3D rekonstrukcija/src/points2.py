import numpy as np

def norma(vektor):
    return [x / vektor[-1] for x in vektor]

def proizvod(a, b, c, d, e, f, g, h, i, j):
    return norma(np.cross(norma(np.cross(norma(np.cross(norma(np.cross(a, b)), norma(np.cross(c, d)))), e)), norma(np.cross(norma(np.cross(norma(np.cross(f, g)),norma(np.cross(h, i)))), j))))


# x
x1 = np.array([335, 74, 1])
x2 = np.array([497, 55, 1])
x3 = np.array([715, 166, 1])
x4 = np.array([536, 190, 1])
x5 = np.array([328, 291, 1])
x6 = None
x7 = np.array([710, 400, 1])
x8 = np.array([537, 430, 1])
x9 = np.array([262, 341, 1])
x10 = None
x11 = np.array([774, 366, 1])
x12 = np.array([312, 412, 1])
x13 = np.array([265, 585, 1])
x14 = None
x15 = np.array([764, 617, 1])
x16 = np.array([316, 669, 1])
x17 = np.array([92, 629, 1])
x18 = None
x19 = np.array([923, 601, 1])
x20 = np.array([700, 779, 1])
x21 = np.array([98, 826, 1])
x22 = None
x23 = np.array([919, 783, 1])
x24 = np.array([694, 984, 1])



# y
y1 = np.array([393, 73, 1])
y2 = np.array([558, 75, 1])
y3 = np.array([559, 196, 1])
y4 = np.array([365, 195, 1])
y5 = None
y6 = None
y7 = np.array([560, 423, 1])
y8 = np.array([370, 423, 1])
y9 = np.array([275, 313, 1])
y10 = np.array([708, 332, 1])
y11 = np.array([680, 401, 1])
y12 = np.array([231, 380, 1])
y13 = None
y14 = np.array([705, 567, 1])
y15 = np.array([679, 639, 1])
y16 = np.array([246, 614, 1])
y17 = np.array([120, 551, 1])
y18 = None
y19 = np.array([855, 657, 1])
y20 = np.array([452, 776, 1])
y21 = np.array([123, 718, 1])
y22 = None
y23 = np.array([854, 839, 1])
y24 = np.array([459, 971, 1])


# nevidljiva tacke

x6 = proizvod(x8,x7,x4,x3,x5,x8,x5,x4,x1,x7)
x6 = np.round((x6 / x6[-1]))

x10 = proizvod(x9,x12,x16,x13,x11,x16,x15,x12,x11,x9)
x10 = np.round((x10 / x10[-1]))

x14 = proizvod(x12,x11,x16,x15,x13,x9,x12,x16,x13,x15)
x14 = np.round((x14 / x14[-1]))

x18 = proizvod(x20,x19,x23,x24,x17,x17,x20,x21,x24,x19)
x18 = np.round((x18 / x18[-1]))

x22 = proizvod(x20,x19,x24,x23,x21,x17,x20,x24,x21,x23)
x22 = np.round((x22 / x22[-1]))

y5 = proizvod(y8,y4,y7,y3,y1,y4,y1,y3,y2,y8)
y5 = np.round((y5 / y5[-1]))

y6 = proizvod(y3,y7,y5,y1,y2,y1,y4,y3,y2,y7)
y6 = np.round((y6 / y6[-1]))


y13 = proizvod(y15,y16,y10,y9,y14,y16,y12,y15,y11,y9)
y13 = np.round((y13 / y13[-1]))

y18 = proizvod(y17,y20,y24,y21,y19,y20,y19,y23,y24,y17)
y18 = np.round((y18 / y18[-1]))

y22 = proizvod(y17,y20,y21,y24,y23,y20,y19,y24,y23,y21)
y22 = np.round((y22 / y22[-1]))



xx = np.array([x1,x2,x3,x4,x7,x8,x9,x11,x12,x15,x16,x17,x23,x24])
yy = np.array([y1,y2,y3,y4,y7,y8,y9,y11,y12,y15,y16,y17,y23,y24])

img1 = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22, x23, x24])
img2 = np.array([y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16, y17, y18, y19, y20, y21, y22, y23, y24])

