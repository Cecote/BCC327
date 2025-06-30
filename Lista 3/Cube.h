#ifndef CUBE_H
#define CUBE_H

#include "Transform.h"

// Classe representando um cubo com transformação própria
class Cube {
public:
    Cube(float scale = 1.0f);  // Construtor
    void draw();               // Desenha o cubo
    Transform transform;       // Transformações aplicadas ao cubo

private:
    void drawFaces();         // Desenha as faces coloridas
    void drawEdges();         // Desenha as arestas
};

#endif