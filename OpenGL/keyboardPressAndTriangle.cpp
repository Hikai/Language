#include <gl/glut.h>
#include <stdio.h>
#include <Windows.h>

void do_display();
void do_keyboard(unsigned char, int, int);

GLfloat x1 = 0, y1 = 0.5;
GLfloat x2 = 0.5, y2 = -0.5;
GLfloat x3 = -0.5, y3 = -0.5;

int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	glutInitWindowSize(800, 600);
	glutCreateWindow("gl");
	glutDisplayFunc(do_display);
	glutKeyboardFunc(do_keyboard);
	glutMainLoop();
	return 0;
}

void do_display()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glPushMatrix();
	glBegin(GL_TRIANGLES);
	glVertex2f(x1, y1);
	glVertex2f(x2, y2);
	glVertex2f(x3, y3);
	glEnd();
	glPopMatrix();
	glFlush();
}

void do_keyboard(unsigned char key, int x, int y)
{
	switch(key) {
	case 'a' :
		x1 -= 0.1;
		x2 -= 0.1;
		x3 -= 0.1;
		break;
	case 'd' :
		x1 += 0.1;
		x2 += 0.1;
		x3 += 0.1;
		break;
	case 's' :
		y1 -= 0.1;
		y2 -= 0.1;
		y3 -= 0.1;
		break;
	case 'w' :
		y1 += 0.1;
		y2 += 0.1;
		y3 += 0.1;
		break;
	default :
		break;
	}
	glutPostRedisplay();
}
