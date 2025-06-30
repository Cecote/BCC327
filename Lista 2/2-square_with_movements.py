from OpenGL.GL import *           
from OpenGL.GLUT import *        
from OpenGL.GLU import *          

# Dimensões da janela
width, height = 500, 500

# Posição inicial do quadrado (centro da janela)
pos_x, pos_y = width // 2, height // 2

# Tamanho do quadrado
size = 100

# Quantidade de pixels que o quadrado se move por tecla
move_step = 10

def init():
    glClearColor(0.106, 0.710, 0.745, 1.0)  # Define a cor de fundo da janela
    glMatrixMode(GL_PROJECTION)            # Define a matriz de projeção como ativa
    glLoadIdentity()                       # Reseta a matriz de projeção
    gluOrtho2D(0, width, 0, height)        # Define projeção ortográfica 2D

def display():
    glClear(GL_COLOR_BUFFER_BIT)           # Limpa o buffer de cor
    glColor3f(1.0, 1.0, 0.0)               # Cor do quadrado 

    half = size // 2                       # Metade do tamanho do quadrado

    # Desenha o quadrado baseado na posição atual (pos_x, pos_y)
    glBegin(GL_QUADS)
    glVertex2f(pos_x - half, pos_y - half)  # Inferior esquerdo
    glVertex2f(pos_x + half, pos_y - half)  # Inferior direito
    glVertex2f(pos_x + half, pos_y + half)  # Superior direito
    glVertex2f(pos_x - half, pos_y + half)  # Superior esquerdo
    glEnd()

    glFlush()  # Finaliza o desenho e exibe na tela

def special_keys(key, x, y):
    global pos_x, pos_y

    # Move o quadrado conforme a tecla de seta pressionada
    if key == GLUT_KEY_UP:
        pos_y += move_step
    elif key == GLUT_KEY_DOWN:
        pos_y -= move_step
    elif key == GLUT_KEY_LEFT:
        pos_x -= move_step
    elif key == GLUT_KEY_RIGHT:
        pos_x += move_step

    glutPostRedisplay()  # Solicita redesenho da tela após o movimento

def main():
    glutInit()                                # Inicializa o GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Define modo de exibição com buffer único e RGB
    glutInitWindowSize(width, height)         # Define tamanho da janela
    glutInitWindowPosition(100, 100)          # Define posição inicial da janela
    glutCreateWindow(b"Quadrado 2D com Movimento")  # Cria a janela com título
    init()                                    # Configurações iniciais do OpenGL
    glutDisplayFunc(display)                  # Registra a função de desenho
    glutSpecialFunc(special_keys)             # Registra a função de controle por teclas especiais (setas)
    glutMainLoop()                            # Inicia o loop principal do GLUT

if __name__ == "__main__":
    main() 
