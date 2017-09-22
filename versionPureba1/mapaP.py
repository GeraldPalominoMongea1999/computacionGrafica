 #mapa
import OpenGL
import sys
import pygame
from pygame.locals import *
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import numpy as np
import pyglet

# width ancho
width=1000
#alto
height=1000
lado=0.3

display = (width,height)

ESCAPE = '\033'
rotacion=0
def iniciar():
    # iniciar pygame
    #invocar las variables globales para la dimecion de los mapas
    global width
    global height
    global display
    # iniiciamos display
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #encabesado
    pygame.display.set_caption("mapa")
    glutInit(sys.argv)
    #gluPerspective(45,width/height,0.005,1000)
    #glutDisplayFunc(dibujar)
    #glutKeyboardFunc(keyPresed)

def cubo():


    # Set display mode
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutSolidCube(lado)

def cuboWire():
    glColor3f(0,0,0)
    glutWireCube(lado)
def piso():
    glColor3f(0,1,0)
    cubo()
    cuboWire()

def columna():
    total=5
    glColor3f(1,1,0)
    for i in range(0,total):
        glTranslate(0,-0,lado)
        cubo()
    glTranslate(0,0,-lado*total)
    for i in range(0,total):
        glTranslate(0,-0,lado)
        cuboWire()
    glTranslate(0,0,-lado*total)
    glColor3f(1,1,0)
    piso()
def cubos():
    #piso()
    mapa=np.array([[True,False,False,False],
                  [False,False,False,False],
                  [True,False,False,False]])
    #mapa=np.array([[1,0,0,0,0],
    #               [1,1,0,0,0],
    #               [0,0,1,1,0],
    #                [0,0,1,1,0],
    #                [0,0,0,1,1],])
    #mapa=np.ones((100,100))
    tamano0=len(mapa[:,0])
    tamano1=len(mapa[0,:])
    q1=0
    q2=0
    for i in range(0,tamano0):

        glTranslate(0,lado,0)
        q1+=1
        for j in range(0,tamano1):

            glTranslate(lado,0,0)
            q2+=1
            if mapa[i,j]==False:
                piso()
            else:
                columna()
        for def main():
    iniciar()
    dibujar()
        # mantien avierta l ventna hasta quese presione exit

if __name__=="__main__":
    main()j in range(0,tamano1):
            glTranslate(-lado,0,0)
    for i in range(0,tamano0):
        glTranslate(0,-lado,0)

def teclado():
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
            if event.key==pygame.K_a:
                glRotate(1,0,0,0.5)
            if event.key==pygame.K_d:
                glRotate(-1,0,0,0.5)
            if event.key==pygame.K_w:
                glRotate(1,0,0.5,0)
            if event.key==pygame.K_s:
                glRotate(-1,0,0.5,0)
            if event.key==pygame.K_q:
                glRotate(1,0.5,0,0)
            if event.key==pygame.K_e:
                glRotate(-1,0.5,0,0)



            if event.key==pygame.K_UP:
                glTranslate(0,-0.1,0)
            if event.key==pygame.K_DOWN:
                glTranslate(0,0.1,0)
            if event.key==pygame.K_RIGHT:
                glTranslate(-0.1,0.0,0.0)
            if event.key==pygame.K_LEFT:
                glTranslate(0.1,-0.0,-0.0)
            if event.key==pygame.K_o:
                glTranslate(0,0,0.1)
            if event.key==pygame.K_l:
                glTranslate(0,0,-0.1)


angulo=70
angulo2=0
angulo3=0
def dibujar():
    #glRotatef(10, 1, 1, 0)
    glutInit(sys.argv)
    global angulo
    glTranslate(-1,-1,-0)
    global angulo2

    global rotacion
    while True:
        #glTranslate(0,0.1,0)

                    #angulo2-=10
                    #print angulo2
        glClearColor(1.0,1.0,1.0,0.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glRotatef(angulo,-0.1, 0,0.0)
        glRotatef(-angulo2, 0, 0, 0.01)
        glRotatef(-angulo3, 0, 0.01,0)
        teclado()
        cubos()
        glRotatef(angulo3, 0, 0.01,0)
        glRotatef(angulo2, 0, 0, 0.01)
        glRotatef(angulo, 0.1, 0,0)
        #glTranslate(0,-0.001,0.01)

        pygame.display.flip()
def main():
    iniciar()
    dibujar()
        # mantien avierta l ventna hasta quese presione exit

if __name__=="__main__":
    main()
