#ifndef CAMERA_H
#define CAMERA_H

// Estrutura para controle da câmera
struct Camera {
    float angleX = 0;  // Rotação vertical
    float angleY = 0;  // Rotação horizontal
    float zoom = -6.0f; // Zoom (translação em Z)

    void apply(); // Aplica a transformação da câmera
};

#endif