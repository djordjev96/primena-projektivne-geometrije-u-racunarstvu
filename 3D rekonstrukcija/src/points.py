import numpy as np

def norma(vektor):
    return [x / vektor[-1] for x in vektor]

def proizvod(a, b, c, d, e, f, g, h, i, j):
    return norma(np.cross(norma(np.cross(norma(np.cross(norma(np.cross(a, b)), norma(np.cross(c, d)))), e)), norma(np.cross(norma(np.cross(norma(np.cross(f, g)),norma(np.cross(h, i)))), j))))


# x
x1 = np.array([958, 38, 1])
x2 = np.array([1117, 111, 1])
x3 = np.array([874, 285, 1])
x4 = np.array([707, 218, 1])
x9 = np.array([292, 569, 1])
x10 = np.array([770, 969, 1])
x11 = np.array([770, 1465, 1])
x12 = np.array([317, 1057, 1])

# y
y1 = np.array([933, 33, 1])
y2 = np.array([1027, 132, 1])
y3 = np.array([692, 223, 1])
y4 = np.array([595, 123, 1])
y9 = np.array([272, 360, 1])
y10 = np.array([432, 814, 1])
y11 = np.array([414, 1284, 1])
y12 = np.array([258, 818, 1])


# preostale tacke
x5 = None
x6 = np.array([1094, 536, 1])
x7 = np.array([862, 729, 1])
# x8 = np.array([710, 532, 1])
x8 = np.array([710, 648, 1])
x13 = None
x14 = np.array([1487, 598, 1])
# x15 = np.array([1257, 1165, 1])
x15 = np.array([1462, 1079, 1])
x16 = None

y5 = None
y6 = np.array([980, 535, 1])
y7 = np.array([652, 638, 1])
y8 = np.array([567, 532, 1])
y13 = np.array([1077, 269, 1])
y14 = np.array([1303, 700, 1])
y15 = np.array([1257, 1165, 1])
y16 = None

# nevidljive tacke

x5 = proizvod(x4,x8,x6,x2,x1,x1,x4,x3,x2,x8)
x5 = np.round((x5 / x5[-1]))

x13 = proizvod(x9,x10,x11,x12,x14,x11,x15,x10,x14,x9)
x13 = np.round((x13 / x13[-1]))

x16 = proizvod(x10,x14,x11,x15,x12,x9,x10,x11,x12,x15)
x16 = np.round((x16 / x16[-1]))

y5 = proizvod(y4,y8,y6,y2,y1,y1,y4,y3,y2,y8)
y5 = np.round((y5 / y5[-1]))

y16 = proizvod(y10,y14,y11,y15,y12,y9,y10,y11,y12,y15)
y16 = np.round((y16 / y16[-1]))


xx = np.array([x1,x2,x3,x4,x9,x10,x11,x12])
yy = np.array([y1,y2,y3,y4,y9,y10,y11,y12])

img1 = np.array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16])
img2 = np.array([y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15, y16])

