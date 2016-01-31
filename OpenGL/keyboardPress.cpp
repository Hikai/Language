#include <gl/glut.h>
#include <stdio.h>
#include <Windows.h>

void do_display();
void do_keyboard(unsigned char, int, int);

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
	glFlush();
}

void do_keyboard(unsigned char key, int x, int y)
{
	switch(key) {
	case 'a' :
		glutSetWindowTitle("a");
		break;
	case 'b' :
		glutSetWindowTitle("b");
		break;
	case 'c' :
		glutSetWindowTitle("c");
		break;
	default :
		glutSetWindowTitle(/*(char *) key*/"?");
	}
	glutPostRedisplay();
}
