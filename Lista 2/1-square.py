from OpenGL.GL import *           
from OpenGL.GLUT import *         
from OpenGL.GLU import *          

# Dimensões da janela
width, height = 500, 500

def init():
    glClearColor(0.106, 0.710, 0.745, 1.0)  # Define a cor de fundo da janela
    glMatrixMode(GL_PROJECTION)      # Define a matriz de projeção como ativa
    glLoadIdentity()                 # Reseta a matriz de projeção
    gluOrtho2D(0, width, 0, height)  # Define uma projeção ortográfica 2D com origem no canto inferior esquerdo

def display():
    glClear(GL_COLOR_BUFFER_BIT)     # Limpa o buffer de cor

    glColor3f(1.0, 1.0, 0.0)         # Define a cor do objeto a ser desenhado

    size = 100                       # Tamanho do lado do quadrado
    cx, cy = width // 2, height // 2  # Coordenadas do centro da janela

    # Inicia o desenho de um quadrado (4 vértices)
    glBegin(GL_QUADS)
    glVertex2f(cx - size / 2, cy - size / 2)  # Vértice inferior esquerdo
    glVertex2f(cx + size / 2, cy - size / 2)  # Vértice inferior direito
    glVertex2f(cx + size / 2, cy + size / 2)  # Vértice superior direito
    glVertex2f(cx - size / 2, cy + size / 2)  # Vértice superior esquerdo
    glEnd()

    glFlush()  # Finaliza o desenho e exibe na tela
    
def main():
    glutInit()                                # Inicializa o GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # Usa modo de exibição com buffer único e cores RGB
    glutInitWindowSize(width, height)         # Define o tamanho da janela
    glutInitWindowPosition(100, 100)          # Define a posição inicial da janela na tela
    glutCreateWindow(b"Quadrado 2D com OpenGL")  # Cria a janela com um título
    init()                                    # Configurações iniciais de OpenGL
    glutDisplayFunc(display)                  # Registra a função de desenho (display)
    glutMainLoop()                            # Inicia o loop principal do GLUT

if __name__ == "__main__":
    main()
