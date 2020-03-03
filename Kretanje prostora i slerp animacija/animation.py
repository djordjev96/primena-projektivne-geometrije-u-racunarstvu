from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
from functions import *

q1 = []
q2 = []
activeTimer = False
t = 0
tm = 40

# pocetne koordinate
x1 = -7
y1 = 5
z1 = 5

# krajnje koordinate
x2 = 5
y2 = 4
z2 = -1

#pocetni uglovi
fi1 = -math.pi/3
psi1 = math.pi/2
teta1 = math.pi/5

#krajnji uglovi
fi2 = 2*math.pi/3
psi2 = -math.pi/4
teta2 = 7*math.pi/8

def showScreen():
    
    # parametri svetla
    light_position = [0, 7, 0, 0]
    light_ambient = [0.5, 0.5, 0.5, 0.1]
    light_diffuse = [0.8, 0.8, 0.8, 1]
    light_specular = [0.6, 0.6, 0.6, 1]
    shininess = 30

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glEnable(GL_NORMALIZE)

    # podesava se tacka pogleda
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(8, 12, 8,
              0, 0, 0,
              0, 1, 0)

    # objekti zadrzavaju boju
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    # podesava se svetlo
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    glLightfv(GL_LIGHT0, GL_POSITION, light_position)
    glLightfv(GL_LIGHT0, GL_AMBIENT, light_ambient)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, light_diffuse)
    glLightfv(GL_LIGHT0, GL_SPECULAR, light_specular)
    glMaterialf(GL_FRONT, GL_SHININESS, shininess)

    drawCoordinateSystem(12)
    drawObject(x1, y1, z1, fi1, teta1, psi1)
    drawObject(x2, y2, z2, fi2, teta2, psi2)

    drawAnimation()

    glutSwapBuffers()

def drawCoordinateSystem(size):
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(size, 0, 0)

    glColor3f(0, 1, 0)
    glVertex3f(0, 0, 0)
    glVertex3f(0, size, 0)

    glColor3f(0, 0, 1)
    glVertex3f(0, 0, 0)
    glVertex3f(0, 0, size)
    glEnd()

def drawObject(x,y,z,fi,teta,psi):
    glPushMatrix()

    glTranslatef(x, y, z)

    A = Euler2A(fi, teta, psi)
    p, alfa = AxisAngle(A)

    glRotatef(alfa / math.pi * 180, p[0], p[1], p[2])
    glutWireCube(1.5)
    
    drawCoordinateSystem(4)

    glPopMatrix()

def drawAnimation():
    glPushMatrix()

    x = (1 - t/tm)*x1 + (t/tm)*x2
    y = (1 - t/tm)*y1 + (t/tm)*y2
    z = (1 - t/tm)*z1 + (t/tm)*z2

    glTranslatef(x,y,z)

    q = Slerp(q1, q2, tm, t)
    p, fi = Q2AxisAngle(q)

    

    glRotatef(fi/math.pi*180, p[0], p[1], p[2])

    glutWireCube(1.5)
    drawCoordinateSystem(4)

    glPopMatrix()



    

def onReshape(w, h):
    glViewport(0, 0, w, h)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60, float(w) / h, 1, 1500)


def onKeyboard(key, x, y):
    global activeTimer
    if ord(key) == 27:
        sys.exit(0)
    elif ord(key) == ord('g') or ord(key) == ord('G'):
        if not activeTimer:
            glutTimerFunc(100, onTimer, 0)
            activeTimer = True
    elif ord(key) == ord('s') or ord(key) == ord('S'):
        activeTimer = False

def onTimer(value):
    global t, activeTimer
    t = t + 1
    if t > tm:
        t = 0
        activeTimer = False
        return

    glutPostRedisplay()
    
    if activeTimer:
        glutTimerFunc(100, onTimer, 0)


def main():
    global q1,q2
    A = Euler2A(fi1, teta1, psi1)
    p, fi = AxisAngle(A)
    q1 = AxisAngle2Q(p, fi)

    A = Euler2A(fi2, teta2, psi2)
    p, fi = AxisAngle(A)
    q2 = AxisAngle2Q(p, fi)
    
    

    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH) 
    glutInitWindowSize(800, 600)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Slerp animation")


    glutDisplayFunc(showScreen)
    glutReshapeFunc(onReshape)
    glutKeyboardFunc(onKeyboard)
    glMatrixMode(GL_PROJECTION)

    glEnable(GL_DEPTH_TEST)

    glutMainLoop() 

if __name__ == '__main__':
    main()