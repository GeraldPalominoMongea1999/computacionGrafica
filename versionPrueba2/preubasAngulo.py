SCREEN_SIZE = (800, 600)
from math import radians
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import pygame
from pygame.locals import *
import time
import numpy as np


def resize(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90.0, float(width)/height, .1, 1000.)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
def init():
    glEnable(GL_TEXTURE_2D)
    glClearColor(0, 1, 1, 1)
    glutInit()
def cargarImagen(nombre):
    # Load the textures
    texture_surface = pygame.image.load(nombre)
    # Retrieve the texture data
    texture_data = pygame.image.tostring(texture_surface, 'RGB', True)
    # Generate a texture id
    texture_id = glGenTextures(1)
    # Tell OpenGL we will be using this texture id for texture operations
    glBindTexture(GL_TEXTURE_2D, texture_id)
    # Tell OpenGL how to scale images
    glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
    glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
    # Tell OpenGL that data is aligned to byte boundries
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1)
    # Get the dimensions of the image
    width, height = texture_surface.get_rect().size
    return (texture_data,width,height)
def cuadrado(v1,v2,v3,v4,nx,ny):
    glBegin(GL_POLYGON)
    glTexCoord2f(0, ny)
    glVertex3fv(v1)
    glTexCoord2f(nx, ny)
    glVertex3fv(v2)
    glTexCoord2f(nx, 0)
    glVertex3fv(v3)
    glTexCoord2f(0, 0)
    glVertex3fv(v4)
    glEnd()
def textureCuadrado(textura,v1,v2,v3,v4,nx,ny):
    glTexImage2D( GL_TEXTURE_2D,
                    0,
                    3,
                    textura[1],
                    textura[2],
                    0,
                    GL_RGB,
                    GL_UNSIGNED_BYTE,
                    textura[0])
    cuadrado(v1,v2,v3,v4,nx,ny)

def eventos(angulo):
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            return
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
                return
            if event.key==pygame.K_a:
                #print "holo"
                angulo+=1
            if event.key==pygame.K_s:
                #print "holo"
                angulo-=1
    return (angulo)
def punto():
    glBegin(GL_POINTS)
    #glPointSize(0.1)
    glColor(1.0, 0.0, 0.0) # Red
    glVertex(0,0,0)
    glEnd()
def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE|OPENGL|DOUBLEBUF)
    resize(*SCREEN_SIZE)
    init()
    v1=(-1, 1, 0)
    v2=(1, 1, 0)
    v3=(1, -1, 0)
    v4=(-1, -1, 0)

    v11=(-0.1, 0.1, 0)
    v12=(0.1, 0.1, 0)
    v13=(0.1, -0.1, 0)
    v14=(-0.1, -0.1, 0)

    v21=(0,-0.3,0)
    v22=(0.4,0.1,0)
    v23=(-0.4,0.1,0)

    angulo=0

    madera=cargarImagen("madera.jpg")
    akari=cargarImagen("akari2.jpg")
    amarillo=cargarImagen("amarillo.png")
    pygame.key.set_repeat(10,10)

    while True:
        angulo=eventos(angulo)
        # Clear the screen (similar to fill)
        glClear(GL_COLOR_BUFFER_BIT)
        # Clear the modelview matrix
        glLoadIdentity()


        glPushMatrix()
        glTranslatef(-1.1, 0.0, -2.0)
        glPushMatrix()

        glRotatef(angulo,0,0,1)
        glTranslate(0,1,0)

        textureCuadrado(madera,v1,v2,v3,v4,1,1)
        #glTranslate(0,-1,0)

        glPopMatrix()
        #textureCuadrado(amarillo,v21,v22,v23,v21,1,1)
        textureCuadrado(akari,v11,v12,v13,v14,1,1)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(1.1, 0.0, -2.0)
        glPushMatrix()

        glTranslate(0,1,0)
        glRotatef(angulo,0,0,1)


        textureCuadrado(madera,v1,v2,v3,v4,1,1)

        glPopMatrix()
        textureCuadrado(amarillo,v21,v22,v23,v21,1,1)
        textureCuadrado(akari,v11,v12,v13,v14,1,1)

        glPopMatrix()

        pygame.display.flip()
        #punto()
        #pygame.display.flip()

if __name__ == "__main__":
    run()
