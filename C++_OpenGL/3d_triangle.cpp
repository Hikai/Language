#include <gl/glut.h>
#include <stdio.h>
#include <Windows.h>

void do_display();
void init_gl();

int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	glutInitDisplayMode(GLUT_DOUBLE);
	glutInitWindowSize(800, 600);
	glutCreateWindow("gl");
	glutDisplayFunc(do_display);
	init_gl();
	glutMainLoop();
	return 0;
}

void do_display()
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	glTranslatef(1.5f, 0, -6.0f);
	glBegin(GL_TRIANGLES);
	glColor3f(1.0f, 0, 0);
	glVertex3f(0, 1.0f, 0);
	glVertex3f(-1.0f, -1.0f, 0);
	glVertex3f(1.0f, -1.0f, 1.0f);
	glColor3f(0, 1.0f, 0);
	glVertex3f(0, 1.0f, 0);
	glVertex3f(1.0f, -1.0f, 1.0f);
	glVertex3f(1.0f, -1.0f, -1.0f);
	glColor3f(0, 0, 1.0f);
	glVertex3f(0, 1.0f, 0);
	glVertex3f(1.0f, -1.0f, -1.0f);
	glVertex3f(-1.0f, -1.0f, -1.0f);
	glColor3f(0, 0, 0);
	glVertex3f(0, 1.0f, 0);
	glVertex3f(-1.0f, -1.0f, -1.0f);
	glVertex3f(-1.0f, -1.0f, 1.0f);
	glEnd();
	glutSwapBuffers();
}

void init_gl()
{
	glClearColor(0, 0, 0, 1.0f);
	glClearDepth(1.0f);
	glEnable(GL_DEPTH_TEST);
	glDepthFunc(GL_LEQUAL);
	glShadeModel(GL_SMOOTH);
	glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST);
}