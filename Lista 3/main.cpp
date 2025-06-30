#include <GL/glut.h>
#include "Cube.h"
#include "Camera.h"

Cube parent(1.0f), child(0.5f); // Cubos pai e filho
Camera cam; // Câmera

void display() {
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    cam.apply(); // Aplica a transformação da câmera

    parent.draw(); // Desenha cubo pai

    glPushMatrix();
        glTranslatef(2.5, 0, 0); // Move cubo filho em relação ao pai
        child.draw();
    glPopMatrix();

    glutSwapBuffers();
}

void reshape(int w, int h) {
    if (h == 0) h = 1;
    float r = w / (float)h;
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45, r, 0.1, 100);
    glMatrixMode(GL_MODELVIEW);
}

void keyboard(unsigned char key, int, int) {
    switch (key) {
        case 'w': cam.angleX -= 5; break;
        case 's': cam.angleX += 5; break;
        case 'a': cam.angleY -= 5; break;
        case 'd': cam.angleY += 5; break;
        case '+': cam.zoom += 0.5; break;
        case '-': cam.zoom -= 0.5; break;
        case 'q': parent.transform.rotY += 5; break;
        case 'e': parent.transform.rotY -= 5; break;
        case 'z': child.transform.rotX += 5; break;
        case 'x': child.transform.rotX -= 5; break;
        case 'r': parent.transform.scale += 0.1; break;
        case 'f': parent.transform.scale -= 0.1; break;
        case 27: exit(0); break; // ESC
    }
    glutPostRedisplay();
}

void initGL() {
    glEnable(GL_BLEND);
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA);
    glEnable(GL_DEPTH_TEST);
    glClearColor(0.9, 0.9, 0.9, 1.0);
}

int main(int argc, char **argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH);
    glutInitWindowSize(800, 600);
    glutCreateWindow("Cena Modularizada: Cubos HSV");

    initGL();
    glutDisplayFunc(display);
    glutReshapeFunc(reshape);
    glutKeyboardFunc(keyboard);

    glutMainLoop();
    return 0;
}