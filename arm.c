#include <GL/gl.h>
#include <GL/glu.h>
#include <GL/glut.h>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

static int shoulder = 270, elbow = 135, elDedo=0 , elDedo2=0, laMano=0,laMano2=0;
static int elDedo3=0;
void init(void)
{
  glClearColor (0.0, 0.0, 0.0, 0.0);
  glShadeModel (GL_FLAT);
}

void display(void)
{
   glClear (GL_COLOR_BUFFER_BIT);
   glPushMatrix();
   glTranslatef (-1.0, 0.0, 0.0);
   glRotatef ((GLfloat) shoulder, 0.0, 0.0, 1.0);
   glTranslatef (1.0, 0.0, 0.0);
   glPushMatrix();
   glScalef (2.0, 0.4, 1.0);
   glutWireCube (1.0);
   glPopMatrix();

   glTranslatef (1.0, 0.0, 0.0);
   glRotatef ((GLfloat) elbow, 0.0, 0.0, 1.0);
   glTranslatef (1.0, 0.0, 0.0);
   glPushMatrix();
   glScalef (2.0, 0.4, 1.0);
   glutWireCube (1.0);
   glPopMatrix();

   glTranslatef (1.0, 0.0, 0.0);
   glRotatef ((GLfloat) laMano, 0.0, 0.0, 1.0);
   glRotatef ((GLfloat) laMano2, 1.0, 0.0, 0.0);
   glTranslatef (0.5, 0.0, 0.0);
   glPushMatrix();
   glScalef (1.0, 0.4, 1.0);
   glutWireCube (1.0);
   glPopMatrix();


   glTranslatef (0.1, 0.0, 0.5);
   glRotatef ((GLfloat) elDedo, 0.0, 0.0, 1.0);
   glTranslatef (1.0, 0.0, 0.0);
   glPushMatrix();
   glScalef (2.0, 0.4, 1.0);
   glutWireCube (0.5);
   glPopMatrix();


   glTranslatef (0.0, 0.0, -1.0);
   glRotatef (30, 0.0, 0.0, 0.0);
   glPushMatrix();
   glScalef (2.0, 0.4, 1.0);
   glutWireCube (0.5);
   glPopMatrix();



   //
   glTranslatef (0.0, 0.0, 0.5);
   //glTranslatef (-2*sin((90-elDedo3)*3.1416/180), 0.0, 0.0);
   glRotatef (90-elDedo3, 0.0, 0.0, 1.0);


   glPushMatrix();
   glScalef (2.0, 0.4, 1.0);
   glutWireCube (0.5);
   glPopMatrix();



   glPopMatrix();
   glutSwapBuffers();
}

void reshape (int w, int h)
{
   glViewport (0, 0, (GLsizei) w, (GLsizei) h);
   glMatrixMode (GL_PROJECTION);
   glLoadIdentity ();
   gluPerspective(65.0, (GLfloat) w/(GLfloat) h, 1.0, 20.0);
   glMatrixMode(GL_MODELVIEW);
   glLoadIdentity();
   glTranslatef (0.0, 0.0, -5.0);
}

void keyboard (unsigned char key, int x, int y)
{
   switch (key) {
      case 's':   /*  s key rotates at shoulder  */
         shoulder = (shoulder + 5) % 360;
         glutPostRedisplay();
         break;
      case 'a':
         shoulder = (shoulder - 5) % 360;
         glutPostRedisplay();
         break;
      case 'd':  /*  e key rotates at elbow  */
         elbow = (elbow + 5) % 360;
         glutPostRedisplay();
         break;
      case 'f':
         elbow = (elbow - 5) % 360;
         glutPostRedisplay();
         break;
      case 'g':  /*  e key rotates at elbow  */
        elDedo = (elDedo + 5) % 360;
        glutPostRedisplay();
        break;
      case 'h':
        elDedo = (elDedo - 5) % 360;
        glutPostRedisplay();
      case 'x':  /*  e key rotates at elbow  */
        elDedo3 = (elDedo3 + 5) % 360;
        glutPostRedisplay();
        break;
      case 'c':
        elDedo3 = (elDedo3 - 5) % 360;
        glutPostRedisplay();



        break;
      case 'm':  /*  e key rotates at elbow  */
        laMano = (laMano + 5) % 360;
        glutPostRedisplay();
        break;
      case 'n':
        laMano = (laMano - 5) % 360;
        glutPostRedisplay();
        break;
      case 'v':
        laMano2 = (laMano2 - 5) % 360;
        glutPostRedisplay();
        break;
      case 'b':  /*  e key rotates at elbow  */
        laMano2 = (laMano2 + 5) % 360;
        glutPostRedisplay();
        break;


      case 27:
          exit(0);
          break;
      default:
         break;
   }
}

int main(int argc, char** argv)
{
   glutInit(&argc, argv);
   glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
   glutInitWindowSize (500, 500);
   glutInitWindowPosition (100, 100);
   glutCreateWindow (argv[0]);
   init ();
   glutDisplayFunc(display);
   glutReshapeFunc(reshape);
   glutKeyboardFunc(keyboard);
   glutMainLoop();
   return 0;
}
