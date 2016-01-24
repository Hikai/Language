#include <gl/glut.h>
#include <Windows.h>

void do_display();
void do_menu(int);

int g_menu = 0;

int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
	glutCreateWindow("gl");
	glutDisplayFunc(do_display);
	glutCreateMenu(do_menu);
	glutAddMenuEntry("BG red", 0);
	glutAddMenuEntry("BG green", 1);
	glutAddMenuEntry("BG blue", 2);
	glutAttachMenu(GLUT_RIGHT_BUTTON);
	glutMainLoop();
	return 0;
}

void do_display()
{
	switch (g_menu) {
	case 0 :
		glClearColor(1, 0, 0, 1.0);
		glClear(GL_COLOR_BUFFER_BIT);
		glFlush();
		break;
	case 1 :
		glClearColor(0, 1, 0, 1.0);
		glClear(GL_COLOR_BUFFER_BIT);
		glFlush();
		break;
	case 2 :
		glClearColor(0, 0, 1, 1.0);
		glClear(GL_COLOR_BUFFER_BIT);
		glFlush();
		break;
	}
}

void do_menu(int menu)
{
	if (menu < 100) {
		g_menu = menu;
		glClearColor(0, 0, 0, 1.0);
		glColor3f(1, 1, 1);
		glutPostRedisplay();
		return;
	}
}