#include "Cube.h"
#include "HSV.h"
#include <GL/glut.h>

Cube::Cube(float s) {
    transform.scale = s; // Define a escala inicial do cubo
}

void Cube::draw() {
    glPushMatrix();
    transform.apply();    // Aplica transformações do cubo
    drawFaces();          // Desenha as faces
    drawEdges();          // Desenha as arestas
    glPopMatrix();
}

void Cube::drawFaces() {
    // Cores HSV para as 6 faces do cubo
    static float hsv[6][3] = {
        {0.0, 1, 1}, {0.2, 1, 1}, {0.4, 1, 1},
        {0.6, 1, 1}, {0.8, 1, 1}, {1.0, 1, 1}
    };
    float r, g, b;
    float a = 0.7; // Transparência

    glBegin(GL_TRIANGLES);
    for (int i = 0; i < 6; ++i) {
        HSVtoRGB(hsv[i][0], hsv[i][1], hsv[i][2], r, g, b);
        glColor4f(r, g, b, a);

        // Duas triangulações por face (total: 12 triângulos)
        switch (i) {
            case 0:
                glVertex3f(-1,-1,1); glVertex3f(1,-1,1); glVertex3f(1,1,1);
                glVertex3f(-1,-1,1); glVertex3f(1,1,1); glVertex3f(-1,1,1);
                break;
            case 1:
                glVertex3f(-1,-1,-1); glVertex3f(-1,1,-1); glVertex3f(1,1,-1);
                glVertex3f(-1,-1,-1); glVertex3f(1,1,-1); glVertex3f(1,-1,-1);
                break;
            case 2:
                glVertex3f(-1,-1,-1); glVertex3f(-1,-1,1); glVertex3f(-1,1,1);
                glVertex3f(-1,-1,-1); glVertex3f(-1,1,1); glVertex3f(-1,1,-1);
                break;
            case 3:
                glVertex3f(1,-1,-1); glVertex3f(1,1,-1); glVertex3f(1,1,1);
                glVertex3f(1,-1,-1); glVertex3f(1,1,1); glVertex3f(1,-1,1);
                break;
            case 4:
                glVertex3f(-1,1,-1); glVertex3f(-1,1,1); glVertex3f(1,1,1);
                glVertex3f(-1,1,-1); glVertex3f(1,1,1); glVertex3f(1,1,-1);
                break;
            case 5:
                glVertex3f(-1,-1,-1); glVertex3f(1,-1,-1); glVertex3f(1,-1,1);
                glVertex3f(-1,-1,-1); glVertex3f(1,-1,1); glVertex3f(-1,-1,1);
                break;
        }
    }
    glEnd();
}

void Cube::drawEdges() {
    glColor3f(0, 0, 0);       // Cor preta para as linhas
    glLineWidth(2);          // Espessura da linha
    glutWireCube(2);         // Desenha as arestas do cubo
}