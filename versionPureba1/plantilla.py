from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def initFun():
    glClearColor(1.0,1.0,1.0,0.0)
    glColor3f(0.0,0.0,0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0.0,640.0,0.0,480.0)

def displayFun():
    glPointSize(4.0)
    glClearColor(1.0,1.0,1.0,0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glBegin(GL_POINTS)
    #width=glutGet(GLUT_WINDOW_WIDTH)
    #height=glutGet(GLUT_WINDOW_HEIGHT)
    #print ("w ",width,"h",height)
    glVertex2i(100,200)

    glEnd()
    glFlush()
if __name__ =='__main__':
    glutInit()
    glutInitWindowSize(640,480)
    glutCreateWindow("base")
    glutInitDisplayMode(GL_COLOR_BUFFER_BIT|GLUT_RGB)
    glutDisplayFunc(displayFun)
    initFun()
    glutMainLoop()
