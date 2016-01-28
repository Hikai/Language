#include <gl/glut.h>
#include <stdio.h>
#include <Windows.h>

void do_display();
void do_mouse(int, int, int, int);
void printw(float, float, float, char *, ...);

GLvoid *font_style = GLUT_BITMAP_TIMES_ROMAN_24;

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
	glBegin(GL_LINE_STRIP);
	glVertex2f(-1.0, 0.7);
	glVertex2f(-0.57, 0.7);
	glEnd();
	glBegin(GL_LINE_STRIP);
	glVertex2f(-0.57, 0.7);
	glVertex2f(-0.15, 0.7);
	glEnd();
	glBegin(GL_LINE_STRIP);
	glVertex2f(-0.57, 0.7);
	glVertex2f(-0.57, 1.0);
	glEnd();
	glBegin(GL_LINE_STRIP);
	glVertex2f(-0.15, 0.7);
	glVertex2f(-0.15, 1.0);
	glEnd();
	glBegin(GL_POLYGON);
	glVertex3f(0.5, 0.5, 0);
	glVertex3f(-0.5, 0.5, 0);
	glVertex3f(0.5, -0.5, 0);
	glVertex3f(-0.5, -0.5, 0);
	glEnd();
	printw(-0.93, 0.8, 0, "Click range");
	printw(-0.52, 0.8, 0, "Second range");
	glFlush();
}

void do_mouse(int button, int state, int x, int y)
{
	char coordination[128];
	if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
		if ((x <= 170) && (y <= 90)) {
			glClearColor(1, 0, 1, 1);
		}
		if ((170 < x) && (x <= 340) && (y <= 90)) {
			glClearColor(1, 1, 0, 1);
		}
	}
	else {
		glClearColor(0, 0, 0, 1);
	}
	glutPostRedisplay();
}

// https://github.com/alibad/Blog/blob/master/OpenGL/OpenGL%20Printw/OpenGL%20Printw/printw.c
void printw(float x, float y, float z, char * format, ...)
{
	va_list args;
	int len;
	int i;
	char * text;
	va_start(args, format);
	len = _vscprintf(format, args) + 1;
	text = (char *)malloc(len * sizeof(char));
	vsprintf_s(text, len, format, args);
	va_end(args);
	glRasterPos3f(x, y, z);
	for (i = 0; text[i] != '\0'; i++) {
		glutBitmapCharacter(font_style, text[i]);
	}
	free(text);
}