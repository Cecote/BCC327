#include "Transform.h"
#include <GL/glut.h>

void Transform::apply() {
    // Aplica transformações na ordem: translação -> rotação -> escala
    glTranslatef(posX, posY, posZ);
    glRotatef(rotX, 1, 0, 0);
    glRotatef(rotY, 0, 1, 0);
    glRotatef(rotZ, 0, 0, 1);
    glScalef(scale, scale, scale);
}