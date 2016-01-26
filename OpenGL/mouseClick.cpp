#include <gl/glut.h>
#include <stdio.h>
#include <Windows.h>

void do_display();
void do_mouse(int, int, int, int);

int APIENTRY WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	glutInitWindowSize(800, 600);
	glutCreateWindow("gl");
	glutDisplayFunc(do_display);
	glutMouseFunc(do_mouse);
	glutMainLoop();
	return 0;
}

void do_display()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(1, 0, 0);
	glBegin(GL_POLYGON);
	glVertex3f(0.5, 0.5, 0);
	glVertex3f(-0.5, 0.5, 0);
	glVertex3f(0.5, -0.5, 0);
	glVertex3f(-0.5, -0.5, 0);
	glEnd();
	glFlush();
}

void do_mouse(int button, int state, int x, int y)
{
	char coordination[128];
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN && x < 170 && y < 90) {
		sprintf_s(coordination, "x = %d, y = %d, good", x, y);
		glClearColor(1, 1, 1, 1);
		glutSetWindowTitle(coordination);
		glutPostRedisplay();
	}
	else {
		glClearColor(0, 0, 0, 0);
		glutPostRedisplay();
	}
}