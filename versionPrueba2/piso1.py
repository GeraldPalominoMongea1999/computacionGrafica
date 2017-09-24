SCREEN_SIZE = (800, 600)
from math import radians
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
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
def rotar(angulo,v ):

    v1=np.sin(angulo)*v[0]+np.cos(angulo)*v[1]
    v2=np.cos(angulo)*v[0]-np.sin(angulo)*v[1]
    return (v1,v2)
def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE|OPENGL|DOUBLEBUF)
    resize(*SCREEN_SIZE)
    init()

    clock = pygame.time.Clock()
    tex_rotation = 0.0
    v1=( 300, -10,300)
    v2=( 300, -10,-300)
    v3=( -300,-10 ,-300)
    v4=( -300,-10, 300)
    angulo = 0
    angulo2=0
    dirX=(1,0)
    dirY=(0,1)
    (posX,posY)=(0,0)
    madera=cargarImagen("madera.jpg")
    pygame.key.set_repeat(10,10)
    while True:
        dirX=(np.cos(angulo*np.pi/180),np.sin(angulo*np.pi/180))
        dirY=(-np.sin((angulo)*np.pi/180),np.cos((angulo)*np.pi/180))
        #dirY=(0,1)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
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
        #time_passed = clock.tick()
        #time_passed_seconds = time_passed / 1000.
        #tex_rotation += time_passed_seconds * 360.0 / 8.0
        # Clear the screen (similar to fill)
        glClear(GL_COLOR_BUFFER_BIT)

        # Clear the modelview matrix
        glLoadIdentity()

        glRotatef(angulo,0,1,0)
        glRotatef(angulo2,1,0,0)
        # Set the modelview matrix

        #glRotate(tex_rotation, 1, 0, 0)
        # Draw a quad (4 vertices, 4 texture coords)

        #glLineWidth(4.0)
        #glBegin(GL_LINES)
        #glVertex3f(0,posX,posY)
        #glVertex3f(0,posX+dirX[0],posY+dirX[1])
        #glEnd()
        glTranslatef(posX, 0, posY)

        textureCuadrado(madera,v1,v2,v3,v4,30,30)

        glTranslatef(-posX, 0, -0.5-posY)
        glutSolidCube(0.2)

        glTranslatef(-5, 10, -5)
        glRotatef(-angulo,0,1,0)

        #glRotate(-90, 0, 0, 1)
        pygame.display.flip()
        # Delete the texture when we are finished with it
    glDeleteTextures(texture_id)
if __name__ == "__main__":
    run()
