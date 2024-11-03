import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# Variáveis de movimento da câmera
camera_x, camera_y, camera_z = 0.0, 0.5, 5.0  # Altura da câmera ajustada
angle_horizontal, angle_vertical = 0.0, 0.0
move_speed = 0.1
rotate_speed = 2.0

# Controle do mouse
last_mouse_x, last_mouse_y = 400, 300  # Posição inicial (meio da tela)
mouse_sensitivity = 0.2

# Função para ajustar a luz
def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    light_pos = [2.0, 5.0, 5.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])

# Função para desenhar as formas geométricas
def draw_shapes():
    # Chão
    glPushMatrix()
    glColor3f(0.5, 0.5, 0.5)
    glBegin(GL_QUADS)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(-10.0, 0.0, 10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glVertex3f(10.0, 0.0, -10.0)
    glEnd()
    glPopMatrix()

    # Cubo
    glPushMatrix()
    glColor3f(1.0, 0.0, 0.0)
    glTranslatef(-2.0, 0.5, -3.0)
    glutSolidCube(1)
    glPopMatrix()

    # Esfera
    glPushMatrix()
    glColor3f(0.0, 1.0, 0.0)
    glTranslatef(1.5, 0.5, -2.0)
    glutSolidSphere(0.5, 32, 32)
    glPopMatrix()

    # Cone
    glPushMatrix()
    glColor3f(0.0, 0.0, 1.0)
    glTranslatef(0.0, 0.5, -5.0)
    glutSolidCone(0.5, 1.0, 32, 32)
    glPopMatrix()

    # Cilindro (orientado no eixo Z para ficar deitado no chão)
    glPushMatrix()
    glColor3f(1.0, 1.0, 0.0)
    glTranslatef(3.0, 0.5, -4.0)
    glRotatef(90, 1, 0, 0)  # Rotaciona o cilindro para deitar no chão
    glutSolidCylinder(0.3, 1.0, 32, 32)
    glPopMatrix()

    # Toroide
    glPushMatrix()
    glColor3f(1.0, 0.5, 0.0)
    glTranslatef(-3.0, 0.5, -5.0)
    glutSolidTorus(0.1, 0.5, 32, 32)
    glPopMatrix()

    # Icosaedro
    glPushMatrix()
    glColor3f(0.0, 1.0, 1.0)
    glTranslatef(2.0, 0.5, -6.0)
    glutSolidIcosahedron()
    glPopMatrix()

    # Dodecaedro
    glPushMatrix()
    glColor3f(0.5, 0.0, 0.5)
    glTranslatef(-2.0, 0.5, -7.0)
    glutSolidDodecahedron()
    glPopMatrix()

# Função para atualizar a câmera
def update_camera():
    gluLookAt(
        camera_x, camera_y, camera_z,
        camera_x + math.sin(math.radians(angle_horizontal)) * math.cos(math.radians(angle_vertical)), 
        camera_y + math.sin(math.radians(angle_vertical)), 
        camera_z - math.cos(math.radians(angle_horizontal)) * math.cos(math.radians(angle_vertical)), 
        0.0, 1.0, 0.0
    )

# Função de exibição
def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    update_camera()
    setup_lighting()
    draw_shapes()
    glutSwapBuffers()

# Funções de controle de movimento
def keyboard(key, x, y):
    global camera_x, camera_y, camera_z
    if key == b'w':
        camera_x += move_speed * math.sin(math.radians(angle_horizontal))
        camera_z -= move_speed * math.cos(math.radians(angle_horizontal))
    elif key == b's':
        camera_x -= move_speed * math.sin(math.radians(angle_horizontal))
        camera_z += move_speed * math.cos(math.radians(angle_horizontal))
    elif key == b'a':
        camera_x -= move_speed * math.cos(math.radians(angle_horizontal))
        camera_z -= move_speed * math.sin(math.radians(angle_horizontal))
    elif key == b'd':
        camera_x += move_speed * math.cos(math.radians(angle_horizontal))
        camera_z += move_speed * math.sin(math.radians(angle_horizontal))
    glutPostRedisplay()

# Função de controle de rotação com o mouse
def mouse_motion(x, y):
    global angle_horizontal, angle_vertical, last_mouse_x, last_mouse_y
    
    dx = x - last_mouse_x
    dy = y - last_mouse_y

    angle_horizontal += dx * mouse_sensitivity
    angle_vertical -= dy * mouse_sensitivity  # Inverte para ajustar ao movimento do mouse

    # Limita o ângulo vertical para evitar rotação completa
    angle_vertical = max(-89.0, min(89.0, angle_vertical))

    last_mouse_x, last_mouse_y = x, y

    glutPostRedisplay()

# Configurações de projeção e perspectiva
def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / float(height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)

# Inicialização da cena
def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1, 0.1, 0.1, 1.0)
    # Centraliza o mouse
    glutWarpPointer(last_mouse_x, last_mouse_y)
    glutSetCursor(GLUT_CURSOR_NONE)  # Esconde o cursor

# Função principal
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"3D Scene with PyOpenGL and Mouse Control")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)  # Atualiza perspectiva ao redimensionar
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(mouse_motion)  # Detecta movimento do mouse
    glutMainLoop()

if __name__ == "__main__":
    main()
