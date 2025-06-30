from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Tamanho da janela
width, height = 500, 500

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Cor de fundo (preto)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, width, 0, height)   # Projeção ortográfica 2D

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Define a cor do quadrado (ex: vermelho)
    glColor3f(1.0, 1.0, 0.0)

    # Tamanho do quadrado
    size = 100
    cx, cy = width // 2, height // 2  # Centro da janela

    # Desenha o quadrado com vértices no sentido anti-horário
    glBegin(GL_QUADS)
    glVertex2f(cx - size / 2, cy - size / 2)  # Canto inferior esquerdo
    glVertex2f(cx + size / 2, cy - size / 2)  # Canto inferior direito
    glVertex2f(cx + size / 2, cy + size / 2)  # Canto superior direito
    glVertex2f(cx - size / 2, cy + size / 2)  # Canto superior esquerdo
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
