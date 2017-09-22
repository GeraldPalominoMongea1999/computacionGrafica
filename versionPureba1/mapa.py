#  mapa
import OpenGL
import sys
import pygame
from pygame.locals import *
from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from PIL import Image
import pyglet
# width ancho
width=640
#alto
height=640


display = (width,height)
def iniciar():
    # iniciar pygame
    pygame.init()
    #invocar las variables globales para la dimecion de los mapas
    global width
    global height
    global display
    # iniiciamos display

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #encabesado
    pygame.display.set_caption("mapa")
def dibujarMapa():





    global width
    global height
    global display
    screen = pygame.display.set_mode(display )
    akari = pygame.image.load("akari.bmp").convert_alpha()
    akari = pygame.transform.scale(akari,(200,200))


    screen.blit(akari, (0, 100))

    pygame.display.update()
    lado=0.5
    glPointSize(10.0)
    glClearColor(1.0,1.0,1.0,0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)

    #pygame.display.set_mode(display, DOUBLEBUF|OPENG)

    glBegin(GL_LINES)

    glVertex3f(lado,lado,0)
    glVertex3f(lado,-lado,0)

    glEnd()

def dibujarMapa2():



    glEnable(GL_TEXTURE_2D)
    akari = pyglet.image.load("akari.jpg")
    texture = akari.get_texture()



    #akari = Image.open('akari.jpg')
    data=pyglet.image.load("akari.jpg").get_data(1,1)
    texture_id = glGenTextures(1)
    akari = glGenTextures(1,akari)

    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, (100), (100), 0, GL_RGBA, GL_UNSIGNED_BYTE, data)
    lado=0.5
    glPointSize(10.0)
    glClearColor(1.0,1.0,1.0,0.0)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0,0.0,0.0)
    glBindTexture(GL_TEXTURE_3D,akari)
    #pygame.display.set_mode(display, DOUBLEBUF|OPENG)

    glBegin(GL_QUADS)

    glVertex3f(lado,lado,0)
    glVertex3f(lado,-lado,0)


    glVertex3f(-lado,lado,0)
    glVertex3f(-lado,-lado,0)

    glVertex3f(-lado,lado,0)
    glVertex3f(lado,lado,0)

    glVertex3f(-lado,-lado,0)
    glVertex3f(lado,-lado,0)
    glEnd()










def dibujar():

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                    sys.exit()

        #screen.fill([255,255,255])
        glRotatef(10, 1, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        dibujarMapa2()
        pygame.display.flip()


def main():
    iniciar()
    dibujar()
        # mantien avierta l ventna hasta quese presione exit

if __name__=="__main__":
    main()
