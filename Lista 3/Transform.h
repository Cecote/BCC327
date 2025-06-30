// Estrutura de transformação com posição, rotação e escala
#ifndef TRANSFORM_H
#define TRANSFORM_H

struct Transform {
    float rotX = 0, rotY = 0, rotZ = 0; // Ângulos de rotação
    float posX = 0, posY = 0, posZ = 0; // Translação
    float scale = 1.0f; // Escala uniforme

    void apply(); // Aplica a transformação via OpenGL
};

#endif