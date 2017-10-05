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
    # Upload the image to OpenGL
    #glTexImage2D( GL_TEXTURE_2D,
    #                0,
    #                3,
    #            width,
    #                height,
    #                0,
    #                GL_RGB,
    #                GL_UNSIGNED_BYTE,
    #                texture_data)
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


def eventos(dirX,dirY,posX,posY,angulo,angulo2):
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
            return
        if event.type == pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE:
                sys.exit()
                return
            if event.key==pygame.K_RIGHT:
                posX-=dirX[0]/5
                posY-=dirX[1]/5
            if event.key==pygame.K_LEFT:
                posX+=dirX[0]/5
                posY+=dirX[1]/5
            if event.key==pygame.K_UP:
                posX+=dirY[0]/5
                posY+=dirY[1]/5
            if event.key==pygame.K_DOWN:
                posX-=dirY[0]/5
                posY-=dirY[1]/5
            if event.key==pygame.K_2:
                angulo+=2
            if event.key==pygame.K_1:
                angulo-=2
            if event.key==pygame.K_3:
                if angulo2<45:
                    angulo2+=2
            if event.key==pygame.K_4:
                if angulo2>-45:
                    angulo2-=2

    return dirX,dirY,posX,posY,angulo,angulo2
def glTranslatefv(paso):
    glTranslate(paso[0],paso[1],paso[2])
def cubo6(cara):
    v11=(-0.25,3,-0.25)
    v12=(-0.25,3,0.25)
    v13=(0.25,3,0.25)
    v14=(0.25,3,-0.25)

    v21=(-0.25,-3,-0.25)
    v22=(-0.25,-3,0.25)
    v23=(0.25,-3,0.25)
    v24=(0.25,-3,-0.25)

    textureCuadrado(cara,v11,v12,v13,v14,1,1)
    textureCuadrado(cara,v21,v22,v23,v24,1,1)

    textureCuadrado(cara,v11,v12,v22,v21,1,6)
    textureCuadrado(cara,v12,v13,v23,v22,1,6)
    textureCuadrado(cara,v13,v14,v24,v23,1,6)
    textureCuadrado(cara,v14,v11,v21,v24,1,6)

def cubo(lado,textura):
    v11=(-lado/2,lado/2*6,-lado/2)
    v12=(-lado/2,lado/2*6,lado/2)
    v13=(lado/2,lado/2*6,lado/2)
    v14=(lado/2,lado/2*3,-lado/2)

    v21=(-lado/2,-lado/2*6,-lado/2)
    v22=(-lado/2,-lado/2*6,lado/2)
    v23=(lado/2,-lado/2*6,lado/2)
    v24=(lado/2,-lado/2*6,-lado/2)

    textureCuadrado(textura,v11,v12,v13,v14,1,1)
    textureCuadrado(textura,v21,v22,v23,v24,1,1)

    textureCuadrado(textura,v11,v12,v22,v21,1,6)
    textureCuadrado(textura,v12,v13,v23,v22,1,6)
    textureCuadrado(textura,v13,v14,v24,v23,1,6)
    textureCuadrado(textura,v14,v11,v21,v24,1,6)


def columna(total,lado,altura,textura):
    total=5
    glTranslate(0,-altura,0)
    for i in range(0,6):
        glTranslate(0,lado,0)
        cubo(lado,textura)
    glTranslate(0,altura-lado*6,0)

def mapa(total,lado,altura,textura):

    m=np.array([[1,1,1,1,1,1],
               [1,0,0,0,0,1],
               [1,0,1,1,0,1],
               [1,0,1,1,0,1],
               [1,0,0,0,0,1],
               [1,1,1,1,1,1]])
    largo=len(m[0,:])
    ancho=len(m[:,0])
    glTranslate(0,0,-total)
    glTranslate(-total,0,0)
    for i in range (0,largo):
        glTranslate(0,0,lado*2)
        for j in range (0,ancho):
            glTranslate(lado*2,0,0)
            if m[i,j]==1:
                glTranslate(0,3*lado,0)
                cubo(lado,textura)
                glTranslate(0,-3*lado,0)
                #columna(total,lado,altura,textura)
        glTranslate(-lado*ancho*2,0,0)
    glTranslate(0,0,-lado*largo*2)

def mapa2(total,lado,altura,textura):
    m=np.array([[1,1,1,1,1,1],
                [0,0,0,0,0,0],
                [0,0,1,1,0,0],
                [0,0,1,1,0,0],
                [0,0,0,0,0,0],
                [1,1,1,1,1,1],
                [0,0,0,0,0,0],
                [1,1,1,1,1,1],
                [0,0,0,0,0,0],
                [0,0,1,1,0,0],
                [0,0,1,1,0,0],
                [0,0,0,0,0,0],
                [1,1,1,1,1,1]
                ])


    largo=len(m[0,:])
    ancho=len(m[:,0])

    glTranslate(0,0,-total)
    glTranslate(-total,0,0)
    glTranslate(0,-3,0)

    for i in range (0,ancho):
        inicio=0
        for j in range (0,largo):
            if (m[i,j]>0 and inicio==0):
                v1=(i*lado*2+lado,0,j*lado*2+lado)
                v2=(i*lado*2+lado,6,j*lado*2+lado)
                inicio=1
            if ((j+1==largo or m[i,j+1]==0) and inicio==1):
                v3=(i*lado*2+lado,0,j*lado*2+lado)
                v4=(i*lado*2+lado,6,j*lado*2+lado)
                inicio=0
                #print "cuandrado"
                textureCuadrado(textura,v2,v1,v3,v4,1,6)


    m=np.array([[1,0,0,0,0,0],
                [1,0,0,0,0,1],
                [1,0,1,1,0,1],
                [1,0,1,1,0,1],
                [1,0,0,0,0,1],
                [1,0,0,0,0,1],
                [0,0,0,0,0,0],
                [1,0,0,0,0,0],
                [1,0,0,0,0,1],
                [1,0,1,1,0,1],
                [1,0,1,1,0,1],
                [1,0,0,0,0,1],
                [1,0,0,0,0,1]
                ])

    for j in range (0,largo):
        inicio=0
        for i in range (0,ancho):
            if (m[i,j]>0 and inicio==0):
                v1=(i*lado*2+lado,0,j*lado*2+lado)
                v2=(i*lado*2+lado,6,j*lado*2+lado)
                inicio=1
            if ((i+1==ancho or m[i+1,j]==0) and inicio==1):
                v3=(i*lado*2+lado,0,j*lado*2+lado)
                v4=(i*lado*2+lado,6,j*lado*2+lado)
                inicio=0
                #print "cuandrado"
                textureCuadrado(textura,v2,v1,v3,v4,1,6)




def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE|OPENGL|DOUBLEBUF)
    resize(*SCREEN_SIZE)
    init()

    #clock = pygame.time.Clock()
    tex_rotation = 0.0

    total=40
    alto=3
    # dimenciones mapa
    v1=( total, -alto,total)
    v2=( total, -alto,-total)
    v3=( -total,-alto ,-total)
    v4=( -total,-alto, total)
    angulo = 0
    angulo2=0
    dirX=(1,0)
    dirY=(0,1)
    (posX,posY)=(total,total)
    # paso a atras de la vista
    pasoAt=(0,0,-0.5)
    pasoAd=(0,0,0.5)

    madera=cargarImagen("madera.jpg")
    pared=cargarImagen("pared.jpg")
    akari=cargarImagen("akari2.jpg")

    pygame.key.set_repeat(10,10)

    while True:

        dirX=(np.cos(angulo*np.pi/180),np.sin(angulo*np.pi/180))
        dirY=(-np.sin((angulo)*np.pi/180),np.cos((angulo)*np.pi/180))
        dirX,dirY,posX,posY,angulo,angulo2=eventos(dirX,dirY,posX,posY,angulo,angulo2)
        # Clear the screen (similar to fill)
        glClear(GL_COLOR_BUFFER_BIT)

        # Clear the modelview matrix
        glLoadIdentity()
        #glTranslatef(0.0,0.0,-1.0)
        #glRotatef(90,1,0,0)


        glRotatef(angulo2,1,0,0)
        glPushMatrix()




        glTranslatef(0.0,0.0,-2.0)
        glRotatef(angulo,0,1,0)

        #
        # mapa
        glPushMatrix()
        glTranslatef(posX, 0, posY)

        textureCuadrado(madera,v1,v2,v3,v4,30,30)
        mapa2(total,1,alto-1,pared)
        glPopMatrix()
        glPopMatrix()
        glTranslatef(0.0,0.0,-2.0)

        cubo6(akari)

        #glTranslatef(-posX, 0, -posY)
        #personajje
        #glTranslatefv((np.sin((angulo)*np.pi/180),0,1-np.cos((angulo)*np.pi/180)))

        #glTranslatef(0.0,0.0,-1.0)
        #glRotatef(-angulo,0,1,0)
        #glPushMatrix()

        #glTranslatef(0, 0.0,-2)


        #glPopMatrix()




        #glTranslatef(0, 0.0,0.5)
        #glutSolidCube(0.1)
        #glRotatef(-angulo2,0,0,0)
        #glTranslatef(-posX, 0, -posY)

        #glRotate(-90, 0, 0, 1)
        pygame.display.flip()
        # Delete the texture when we are finished with it
    glDeleteTextures(texture_id)
if __name__ == "__main__":
    run()
