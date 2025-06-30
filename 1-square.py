from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


width, height = 500, 500

def init():
    glClearColor(0.106, 0.710, 0.745, 1.0)  
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    
    glColor3f(1.0, 0.0, 0.0)

    
    size = 100
    cx, cy = width // 2, height // 2  

    
    glBegin(GL_QUADS)
    glVertex2f(cx - size / 2, cy - size / 2)  
    glVertex2f(cx + size / 2, cy - size / 2)  
    glVertex2f(cx + size / 2, cy + size / 2)  
    glVertex2f(cx - size / 2, cy + size / 2)  
    glEnd()

    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Quadrado 2D com OpenGL")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()
