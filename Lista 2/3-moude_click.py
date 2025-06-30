from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


width, height = 800, 600

def mouse_click(button, state, x, y):
    if state == GLUT_DOWN:
        print(f"Coordenadas do clique: ({x}, {height - y})")  

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutInitWindowPosition(100, 100)
    glutCreateWindow(b"Deteccao de Cliques do Mouse")
    
    
    glClearColor(0.106, 0.710, 0.745, 1.0) 

    
    glutDisplayFunc(display)

    
    glutMouseFunc(mouse_click)

    glutMainLoop()

if __name__ == "__main__":
    main()
