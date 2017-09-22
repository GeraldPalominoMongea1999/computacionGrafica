import OpenGL
import sys
import pygame
from pygame.locals import *
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#abriendo una ventna con pygame


# width ancho
width=640
#alto
height=640
def cuadrado():
    lado=0.5
    glPointSize(10.0)
    glClearColor(1.0,1.0,1.0,0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)

    glVertex3f(lado,lado,0)
    glVertex3f(lado,-lado,0)

    glVertex3f(-lado,lado,0)
    glVertex3f(-lado,-lado,0)

    glVertex3f(-lado,lado,0)
    glVertex3f(lado,lado,0)

    glVertex3f(-lado,-lado,0)
    glVertex3f(lado,-lado,0)

    #glVertex3f(0.0,0.0,0)
    #glVertex3f(lado,lado,0)

    #glVertex3f(0,0.5,0)
    #glVertex3f(0.1,0,0)
    glEnd()

def main():
    # inicia la ventna
    pygame.init()

    display = (width,height)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    # edimeciones de la ventna
    #screen=pygame.display.set_mode((width,height))


    # encaesado de la ventna
    pygame.display.set_caption("tutorial pygame")



    # mantien avierta l ventna hasta quese presione exit

    while True:

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    sys.exit()

        #screen.fill([255,255,255])
        glRotatef(10, 0.9, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cuadrado()
        pygame.display.flip()
if __name__=='__main__':
    main()
