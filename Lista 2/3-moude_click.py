from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


width, height = 800, 600  # Dimensões da janela

def mouse_click(button, state, x, y):
    if state == GLUT_DOWN:
        # Imprime as coordenadas do clique com ajuste no eixo Y (origem no canto inferior)
        print(f"Coordenadas do clique: ({x}, {height - y})")  

def display():
    glClear(GL_COLOR_BUFFER_BIT)  # Limpa o buffer de cor
    glFlush()                     # Finaliza o desenho e exibe

def main():
    glutInit()                                 # Inicializa o GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Define modo com buffer único e RGB
    glutInitWindowSize(width, height)          # Define tamanho da janela
    glutInitWindowPosition(100, 100)           # Define posição inicial da janela
    glutCreateWindow(b"Deteccao de Cliques do Mouse")  # Cria a janela com título
    
    glClearColor(0.106, 0.710, 0.745, 1.0)      # Define a cor de fundo da janela
    
    glutDisplayFunc(display)                   # Registra a função de desenho
    
    glutMouseFunc(mouse_click)                 # Registra a função para capturar cliques do mouse

    glutMainLoop()                             # Inicia o loop principal do GLUT

if __name__ == "__main__":
    main() 
