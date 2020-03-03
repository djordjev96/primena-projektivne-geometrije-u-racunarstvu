import numpy as np
from functools import reduce
from tkinter import Tk, Button, Canvas, Frame, BOTH, Label
from PIL import Image, ImageTk
import cv2
import matplotlib.pyplot as plt

pathToImage = "input2.jpg"
# pathToImage = "input.png"
imageWH = Image.open(pathToImage)
width, height = imageWH.size
selectedPoints = []
# fixedImages = [(300, 100, 1), (600, 100, 1), (600, 400, 1), (300, 400, 1)]
fixedImages = [(0, 0, 1), (0, height/2, 1), (width/2, height/2, 1), (width/2, 0, 1)]

def naiveAlgorythm(points, images):
    delta = np.linalg.det(np.column_stack((points[0],points[1],points[2])))    
    delta1 = np.linalg.det(np.column_stack((points[3], points[1], points[2])))
    delta2 = np.linalg.det(np.column_stack((points[0], points[2], points[3])))
    delta3 = np.linalg.det(np.column_stack((points[0], points[1], points[3])))

    lambda1 = delta1/delta
    lambda2 = delta2/delta
    lambda3 = delta3/delta

    delta_ = np.linalg.det(np.column_stack((images[0],images[1],images[2])))    
    delta1_ = np.linalg.det(np.column_stack((images[3], images[1], images[2])))
    delta2_ = np.linalg.det(np.column_stack((images[0], images[2], images[3])))
    delta3_ = np.linalg.det(np.column_stack((images[0], images[1], images[3])))

    p1 = np.column_stack((points[0]*lambda1, points[1]*lambda2, points[2]*lambda3))

    lambda1_ = delta1_/delta_
    lambda2_ = delta2_/delta_
    lambda3_ = delta3_/delta_

    p2 = np.column_stack((images[0]*lambda1_, images[1]*lambda2_, images[2]*lambda3_))

    p = np.dot(p2,np.linalg.inv(p1))

    return p

def DLT(points, images):    
    A = []
    for i in range(4):
        x1, x2, x3 = points[i,0], points[i,1], points[i,2]
        x1_, x2_, x3_ = images[i,0], images[i,1], images[i,2]
        A.append([0, 0, 0, -x3_*x1, -x3_*x2, -x3_*x3, x2_*x1, x2_*x2, x2_*x3])
        A.append([x3_*x1, x3_*x2, x3_*x3, 0, 0, 0, -x1_*x1, -x1_*x2, -x1_*x3])
    A = np.asarray(A)
    U, D, V_T = np.linalg.svd(A)
    V_T = np.around(V_T, 5)
    return V_T[-1,:].reshape(3,3)        


def comparisonNaiveDLT(naive, dlt):
    dlt = np.dot(np.true_divide(dlt,dlt[0,0]),naive[0,0])
    print(dlt)

def normalizationMatrix(points):
    n = len(points)

    cx = sum(map(lambda point: point[0]/point[2], points))/n
    cy = sum(map(lambda point: point[1]/point[2], points))/n

    c = (cx,cy)

    G = np.array([[1, 0, -c[0]],
                  [0, 1, -c[1]],
                  [0, 0, 1]])

    sumDistance = 0
    for point in points:
        sumDistance += np.sqrt((c[0] - point[0]/point[2])**2 + (c[1] - point[1]/point[2])**2)
    avg = sumDistance/n
    k = np.sqrt(2)/avg
    S = np.array([
        [k, 0, 0],
        [0, k, 0],
        [0, 0, 1]
      ])

    T = np.dot(S,G)
    return T

def applyTransformation(T, vertices):
    newVertices = []
    for v in vertices:
        newVertices.append(np.dot(T, np.transpose(v)))

    return newVertices

def normalizedDLT(points, images):
    T = normalizationMatrix(points)
    Tp = normalizationMatrix(images)

    newPoints = np.array(applyTransformation(T, points))
    newImages = np.array(applyTransformation(Tp, images))


    pp = DLT(newPoints, newImages)

    p = np.dot(np.dot(np.linalg.inv(Tp), pp), T)
    return np.around(p, 5)

def onClickFunction(event):    
    if len(selectedPoints) < 4:
        selectedPoints.append((event.x, event.y, 1))
        print("Position = ({0},{1})".format(event.x, event.y))
    
def resetPoints():
    selectedPoints.clear()
    print(selectedPoints)

def fixImage():
    if len(selectedPoints) == 4:
        P = normalizedDLT(selectedPoints, fixedImages)
        
        img = cv2.imread(pathToImage)
        height, width, channels = img.shape
        dst = cv2.warpPerspective(img,P,(width, height))

        plt.subplot(121),plt.imshow(img),plt.title('Input')
        plt.subplot(122),plt.imshow(dst),plt.title('Output')
        plt.show()

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open(pathToImage)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
        img.bind('<Button-1>', onClickFunction)

        resetButton = Button(master,
                              text='Reset points',
                              highlightcolor='blue',
                              activebackground='blue',
                              activeforeground='white',
                              command=resetPoints)
        resetButton.pack()


        fixButton = Button(master,
                            text='Fix distortion',
                            highlightcolor='blue',
                            activebackground='blue',
                            activeforeground='white',
                            command=fixImage)
        fixButton.pack()

if __name__ == "__main__":

    # points = list(map(float,input().split()))
    # for i in range(4):
    #     points[i,0], points[i,1], points[i,2] = input().split()


    points = np.array([
                       [-3, -1, 1], 
                       [3, -1, 1], 
                       [1, 1, 1], 
                       [-1, 1, 1],
                       [1, 2, 3],
                       [-8, -2, 1]
                      ])

    # points = np.array([
    #                    [1, 1, 1], 
    #                    [5, 2, 1], 
    #                    [6, 4, 1], 
    #                    [-1, 7, 1],
    #                 #    [3, 1, 1],
    #                   ])
    

    # for i in range(4):
    #     images[i,0], images[i,1], images[i,2] = input().split()

    images = np.array([
                       [-2, -1, 1], 
                       [2, -1 , 1], 
                       [2, 1, 1], 
                       [-2, 1, 1],
                       [2, 1, 4],
                       [-16, -5, 4]
                      ])

    # images = np.array([
    #                    [0, 0, 1], 
    #                    [10, 0 , 1], 
    #                    [10, 5, 1], 
    #                    [0, 5, 1],
    #                 #    [3, -1, 1],
    #                   ])
    

    naive = naiveAlgorythm(points, images)
    print(naive)
    dlt = DLT(points, images)
    print(dlt)
    # comparisonNaiveDLT(naive, dlt)

    nDLT = normalizedDLT(points, images)
    print(nDLT)
        
    root = Tk()
    app = Window(root)
    root.wm_title("Tkinter window")
    root.geometry('800x600')
    root.mainloop()