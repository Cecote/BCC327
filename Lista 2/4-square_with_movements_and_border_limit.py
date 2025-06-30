from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

width, height = 500, 500  # Dimensões da janela

# Posição inicial do quadrado (centro da janela)
pos_x, pos_y = width // 2, height // 2

size = 100                # Tamanho do quadrado
move_step = 10            # Quantidade de pixels que o quadrado se move por tecla

def init():
    glClearColor(0.106, 0.710, 0.745, 1.0)  # Define a cor de fundo da janela
    glMatrixMode(GL_PROJECTION)            # Seleciona a matriz de projeção
    glLoadIdentity()                       # Reseta a matriz
    gluOrtho2D(0, width, 0, height)        # Define projeção ortográfica 2D

def display():
    glClear(GL_COLOR_BUFFER_BIT)           # Limpa o buffer de cor
    glColor3f(1.0, 1.0, 0.0)               # Cor do quadrado (amarelo)

    half = size // 2                       # Metade do tamanho do quadrado

    # Desenha o quadrado na posição atual
    glBegin(GL_QUADS)
    glVertex2f(pos_x - half, pos_y - half)  # Vértice inferior esquerdo
    glVertex2f(pos_x + half, pos_y - half)  # Vértice inferior direito
    glVertex2f(pos_x + half, pos_y + half)  # Vértice superior direito
    glVertex2f(pos_x - half, pos_y + half)  # Vértice superior esquerdo
    glEnd()

    glFlush()  # Finaliza o desenho e exibe

def special_keys(key, x, y):
    global pos_x, pos_y

    half = size // 2  # Usado para limitar movimento dentro da janela

    # Verifica tecla pressionada e move o quadrado se estiver dentro dos limites
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

    glutPostRedisplay()  # Solicita redesenho da janela

def main():
    glutInit()                                # Inicializa o GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Define modo com buffer único e RGB
    glutInitWindowSize(width, height)         # Define tamanho da janela
    glutInitWindowPosition(100, 100)          # Define posição inicial da janela
    glutCreateWindow(b"Quadrado 2D com Movimento")  # Cria a janela com título
    init()                                    # Configurações iniciais do OpenGL
    glutDisplayFunc(display)                  # Registra a função de desenho
    glutSpecialFunc(special_keys)             # Registra a função para teclas especiais (setas)
    glutMainLoop()                            # Inicia o loop principal

if __name__ == "__main__":
    main()  # Executa o programa
