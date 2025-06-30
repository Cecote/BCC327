from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


width, height = 500, 500


pos_x, pos_y = width // 2, height // 2


size = 100


move_step = 10

def init():
    glClearColor(0.106, 0.710, 0.745, 1.0) 
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1.0, 1.0, 0.0)

    half = size // 2

    glBegin(GL_QUADS)
    glVertex2f(pos_x - half, pos_y - half)
    glVertex2f(pos_x + half, pos_y - half)
    glVertex2f(pos_x + half, pos_y + half)
    glVertex2f(pos_x - half, pos_y + half)
    glEnd()

    glFlush()

def special_keys(key, x, y):
    global pos_x, pos_y

    half = size // 2

    if key == GLUT_KEY_UP:
        if pos_y + half + move_step <= height:
            pos_y += move_step
    elif key == GLUT_KEY_DOWN:
        if pos_y - half - move_step >= 0:
            pos_y -= move_step
    elif key == GLUT_KEY_LEFT:
        if pos_x - half - move_step >= 0:
            pos_x -= move_step
    elif key == GLUT_KEY_RIGHT:
        if pos_x + half + move_step <= width:
            pos_x += move_step

    glutPostRedisplay()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Quadrado 2D com Movimento")
    init()
    glutDisplayFunc(display)
    glutSpecialFunc(special_keys)
    glutMainLoop()

if __name__ == "__main__":
    main()
