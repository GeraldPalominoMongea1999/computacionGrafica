SCREEN_SIZE = (800, 600)
from math import radians
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import time
import numpy
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
def cuadrado(v1,v2,v3,v4):
    glBegin(GL_POLYGON)
    glTexCoord2f(0, 3)
    glVertex3fv(v1)
    glTexCoord2f(3, 3)
    glVertex3fv(v2)
    glTexCoord2f(3, 0)
    glVertex3fv(v3)
    glTexCoord2f(0, 0)
    glVertex3fv(v4)
    glEnd()
def textureCuadrado(textura,v1,v2,v3,v4):
    glTexImage2D( GL_TEXTURE_2D,
                    0,
                    3,
                    textura[1],
                    textura[2],
                    0,
                    GL_RGB,
                    GL_UNSIGNED_BYTE,
                    textura[0])
    cuadrado(v1,v2,v3,v4)

def run():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE|OPENGL|DOUBLEBUF)
    resize(*SCREEN_SIZE)
    init()

    clock = pygame.time.Clock()
    tex_rotation = 0.0
    v1=(-300, 300, 0)
    v2=(300, 300, 0)
    v3=(300, -300, 0)
    v4=(-300, -300, 0)

    v5=(300, 300*numpy.sqrt(2)/2, -600)
    v6=(-300, 300*numpy.sqrt(2)/2, -600)
    print "lol"
    satania=cargarImagen("satania1.jpg")
    akari=cargarImagen("akari1.jpg")
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    return
        #time_passed = clock.tick()
        #time_passed_seconds = time_passed / 1000.
        #tex_rotation += time_passed_seconds * 360.0 / 8.0
        tex_rotation+=1
        if tex_rotation>=360:
            tex_rotation=0
        # Clear the screen (similar to fill)
        glClear(GL_COLOR_BUFFER_BIT)
        # Clear the modelview matrix
        glLoadIdentity()

        # Set the modelview matrix
        glTranslatef(0.0, 0.0, -600.0)
        glRotate(tex_rotation, 1, 0, 0)
        glRotate(90, 0, 0, 1)
        # Draw a quad (4 vertices, 4 texture coords)
        if tex_rotation>90 and tex_rotation<270:
            textureCuadrado(satania,v1,v2,v3,v4)
            textureCuadrado(akari,v1,v2,v5,v6)
        else:
            textureCuadrado(akari,v1,v2,v5,v6)
            textureCuadrado(satania,v1,v2,v3,v4)


        glRotate(-90, 0, 0, 1)
        pygame.display.flip()
        # Delete the texture when we are finished with it
    glDeleteTextures(texture_id)
if __name__ == "__main__":
    run()
