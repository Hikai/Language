#include <gl/glut.h>
#include <Windows.h>

void do_display();
void do_menu(int);

int g_menu = 0;

int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	glutCreateWindow("gl");
	GLint sub_menu = glutCreateMenu(do_menu);
	glutAddMenuEntry("red", 1);
	glutAddMenuEntry("green", 2);
	glutAddMenuEntry("blue", 3);
	glutCreateMenu(do_menu);
	glutAddMenuEntry("white", 0);
	glutAddSubMenu("quads", sub_menu);
	glutAttachMenu(GLUT_RIGHT_BUTTON);
	glutDisplayFunc(do_display);
	glColor3f(1.0, 0.0, 0.0);
	glutMainLoop();
	return 0;
}

void do_display()
{
	glClear(GL_COLOR_BUFFER_BIT);
	glBegin(GL_QUADS);
	glVertex2f(0.5, 0.5);
	glVertex2f(-0.5, 0.5);
	glVertex2f(0.5, -0.5);
	glVertex2f(-0.5, -0.5);
	glEnd();
	glFlush();
}

void do_menu(int menu)
{
	switch (menu) {
	case 0 :
		glClearColor(1, 1, 1, 1);
		break;
	case 1 :
		glColor3f(1, 0, 0);
		break;
	case 2 :
		glColor3f(0, 1, 0);
		break;
	case 3 :
		glColor3f(0, 0, 1);
		break;
	}
	glutPostRedisplay();
}