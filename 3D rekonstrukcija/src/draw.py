from OpenGL.GL   import *
from OpenGL.GLU  import *
from OpenGL.GLUT import *
import points as pts
import algorythms as alg
import numpy as np

def init(args):
    glutInit(args)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DEPTH | GLUT_DOUBLE)

    glutInitWindowSize(1000, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("3D Reconstruction")
    
    glutReshapeFunc(on_reshape)
    glutDisplayFunc(on_display)
    
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_NORMALIZE)

    glClearColor(0.120, 0.120, 0.120, 0)
    glShadeModel(GL_SMOOTH)


def on_display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    gluLookAt(
         1000, 800, 1000,
         900,   500,   0,
         0, 0, 1
    )

    # gluLookAt(
    #      600, 600, 600,
    #      0,   0,   0,
    #      0, 1, 0
    # )
    drawObjects()

    glutSwapBuffers()

def on_reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, float(width) / float(height), 1, 1500)

def drawObjects():
    ff, e = alg.get_ff_and_e(pts.xx, pts.yy)

    rekonstruisane = []

    for i in range(len(pts.img1)):
        rekonstruisane.append(alg.triangulation(pts.img1[i], pts.img2[i], e, ff))
    
    rek = np.array(rekonstruisane)

    draw_first(rek)
    draw_second(rek)
    # draw_third(rek)

    
def draw_first(rek):
    glLineWidth(2)
    
    glBegin(GL_LINES)
    glColor3ub(243, 0, 0)

    ivice = np.array([[0,1], [1,2], [2,3], [3,0], [4,5], [5,6], [6,7], [7,4], [0,4], [1,5], [2,6], [3,7]])
    

    for (x,y) in ivice:
        glVertex3f(rek[x][0], rek[x][1], rek[x][2])
        glVertex3f(rek[y][0], rek[y][1], rek[y][2])

    glEnd()

def draw_second(rek):
    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3ub(0, 0, 240)

    # ivice = np.array([[8,9], [9,10], [10,11], [11,8], [12,13], [13,14], [14,15], [15,12], [8,12], [9,13], [10,14], [11,15]])

    ivice = np.array([[8,9], [9,10], [10,11], [11,8], [12,15], [15,14], [14,13], [13,12], [15,11], [14,10], [8,12], [13,9]])

    
    for (x,y) in ivice:
        glVertex3f(rek[x][0], rek[x][1], rek[x][2])
        glVertex3f(rek[y][0], rek[y][1], rek[y][2])

    glEnd()

def draw_third(rek):
    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3ub(0, 240, 0)

    ivice = np.array([[16,17], [17,18], [18,19], [19,16], [20,21], [21,22], [22,23], [23,20], [16,20], [17,21], [18,22], [19,23]])

    
    for (x,y) in ivice:
        glVertex3f(rek[x][0], rek[x][1], rek[x][2])
        glVertex3f(rek[y][0], rek[y][1], rek[y][2])

    glEnd()

