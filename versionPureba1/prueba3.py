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
width=500
#alto
height=500
lado=0.3

display = (width,height)
def iniciar():
    # iniciar pygame
    #invocar las variables globales para la dimecion de los mapas
    global width
    global height
    global display
    #global screen
    # iniiciamos display
    pygame.init()
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #encabesado
    pygame.display.set_caption("mapa")
    glutInit(sys.argv)
    #gluPerspective(45,width/height,0.005,1000)
    #glutDisplayFunc(dibujar)
    #glutKeyboardFunc(keyPresed)
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

lado=1
def  poligono():
    glBegin(GL_POLYGON)
    glTexCoord2f(1, 1)
    glVertex3f(0.5,0.5,0)
    glTexCoord2f(0, 1)
    glVertex3f(-0.5,0.5,0)
    glTexCoord2f(0, 0)
    glVertex3f(-0.5,-0.5,0)
    glTexCoord2f(1, 0)
    glVertex3f(0.5,-0.5,0)
    glEnd()

def dibujar():
    #glRotatef(10, 1, 1, 0)
    glutInit(sys.argv)
    global angulo
    glTranslate(-1,-1,-0)
    global display

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    while True:


        glClearColor(1.0,1.0,1.0,0.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        teclado()
        akari = pygame.image.load("akari.jpg").convert()

        akari_data = pygame.image.tostring(akari, 'RGB', True)
        #screen=pygame.display.set_mode(display)
        #screen.blit(akari,(0,0))
        texture_id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, texture_id)

        #akari = glGenTextures(1,akari)
        #
        poligono()
        pygame.display.update()



        #pygame.display.flip()
        #teclado()
        #glClearColor(1.0,1.0,1.0,0.0)
        #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #glColor3f(1,0,1)
        #glTranslate(1,1,0)
        #glRotatef(30,0, 0,1.0)
        #glutSolidCube(0.1)


        #glTranslate(-1,-1,-0)
        #pygame.display.flip()

        #window.clear()
        #batch.draw()
        #glBindTexture(GL_TEXTURE_2D,akari)


def main():
    iniciar()
    dibujar()
        # mantien avierta l ventna hasta quese presione exit

if __name__=="__main__":
    main()
