#include "Camera.h"
#include <GL/glut.h>

void Camera::apply() {
    glTranslatef(0, 0, zoom);       // Aplica o zoom
    glRotatef(angleX, 1, 0, 0);     // Rotação vertical
    glRotatef(angleY, 0, 1, 0);     // Rotação horizontal
}