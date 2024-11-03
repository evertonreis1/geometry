import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import random

camera_x, camera_y, camera_z = 0.0, 0.5, 5.0
angle_horizontal, angle_vertical = 0.0, 0.0
move_speed = 0.1
rotate_speed = 2.0

# Definições das câmeras
camera_positions = [
    (0.0, 0.5, 5.0), 
    (5.0, 2.0, 5.0),
    (-5.0, 2.0, 5.0)
]
current_camera_index = 0

last_mouse_x, last_mouse_y = 400, 300
mouse_sensitivity = 0.2

objects = [
    {"name": "Cubo", "description": "Uma forma geométrica de seis faces quadradas.", "position": (-2.0, 0.5, -3.0), "radius": 0.7},
    {"name": "Esfera", "description": "Uma esfera 3D perfeitamente redonda.", "position": (1.5, 0.5, -2.0), "radius": 0.5},
    {"name": "Cone", "description": "Um cone com uma base circular.", "position": (0.0, 0.5, -5.0), "radius": 0.5},
    {"name": "Cilindro", "description": "Um cilindro deitado no chão.", "position": (3.0, 0.5, -4.0), "radius": 0.5},
    {"name": "Toroide", "description": "Um toroide, ou forma de anel.", "position": (-3.0, 0.5, -5.0), "radius": 0.6},
    {"name": "Icosaedro", "description": "Um poliedro com 20 faces triangulares.", "position": (2.0, 0.5, -6.0), "radius": 0.6},
    {"name": "Dodecaedro", "description": "Um poliedro com 12 faces pentagonais.", "position": (-2.0, 0.5, -7.0), "radius": 0.6}
]

current_object = None
last_object = None


def setup_lighting():
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    light_pos = [2.0, 5.0, 5.0, 1.0]
    glLightfv(GL_LIGHT0, GL_POSITION, light_pos)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1.0])
    glLightfv(GL_LIGHT0, GL_SPECULAR, [1.0, 1.0, 1.0, 1.0])


def random_color():
    return (random.random(), random.random(), random.random())


def draw_shapes():
    for obj in objects:
        glPushMatrix()
        glTranslatef(*obj["position"])
        
        if obj["name"] == "Cubo":
            glMaterialfv(GL_FRONT, GL_DIFFUSE, CUBE_COLOR + (1.0,))
            glutSolidCube(1)
        elif obj["name"] == "Esfera":
            glMaterialfv(GL_FRONT, GL_DIFFUSE, SPHERE_COLOR + (1.0,))
            glutSolidSphere(0.5, 32, 32)
        elif obj["name"] == "Cone":
            glMaterialfv(GL_FRONT, GL_DIFFUSE, CONE_COLOR + (1.0,))
            glutSolidCone(0.5, 1.0, 32, 32)
        elif obj["name"] == "Cilindro":
            glMaterialfv(GL_FRONT, GL_DIFFUSE, CYLINDER_COLOR + (1.0,))
            glRotatef(90, 1, 0, 0)
            glutSolidCylinder(0.3, 1.0, 32, 32)
        elif obj["name"] == "Toroide":
            glMaterialfv(GL_FRONT, GL_DIFFUSE, TORUS_COLOR + (1.0,))
            glutSolidTorus(0.1, 0.5, 32, 32)
        elif obj["name"] == "Icosaedro":
            glMaterialfv(GL_FRONT, GL_DIFFUSE, ICOSAHEDRON_COLOR + (1.0,))
            glutSolidIcosahedron()
        elif obj["name"] == "Dodecaedro":
            glMaterialfv(GL_FRONT, GL_DIFFUSE, DODECAHEDRON_COLOR + (1.0,))
            glutSolidDodecahedron()
        
        glPopMatrix()


def draw_ground():
    glBegin(GL_QUADS)
    glColor3f(0.5, 0.5, 0.5)
    glVertex3f(-10.0, 0.0, -10.0)
    glVertex3f(10.0, 0.0, -10.0)
    glVertex3f(10.0, 0.0, 10.0)
    glVertex3f(-10.0, 0.0, 10.0)
    glEnd()


def detect_nearby_object():
    global current_object
    current_object = None
    for obj in objects:
        distance = math.sqrt(
            (camera_x - obj["position"][0]) ** 2 +
            (camera_y - obj["position"][1]) ** 2 +
            (camera_z - obj["position"][2]) ** 2
        )
        if distance < obj["radius"]:
            current_object = obj
            break


def display_text():
    global current_object
    global last_object
    
    if current_object and last_object != current_object:
        print(f"{current_object['name']}: {current_object['description']}")
        last_object = current_object

def update_camera():
    global camera_x, camera_y, camera_z
    
    camera_x, camera_y, camera_z = camera_positions[current_camera_index]
    gluLookAt(
        camera_x, camera_y, camera_z,
        camera_x + math.sin(math.radians(angle_horizontal)) * math.cos(math.radians(angle_vertical)), 
        camera_y + math.sin(math.radians(angle_vertical)), 
        camera_z - math.cos(math.radians(angle_horizontal)) * math.cos(math.radians(angle_vertical)), 
        0.0, 1.0, 0.0
    )


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    update_camera()
    setup_lighting()
    draw_ground()
    draw_shapes()
    detect_nearby_object()
    display_text()
    glutSwapBuffers()


def keyboard(key, x, y):
    global camera_x, camera_y, camera_z, current_camera_index
    
    if current_camera_index == 0:
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
        
        camera_positions[current_camera_index] = (camera_x, camera_y, camera_z)
    if key == b'c':  # Alternar entre câmeras
        current_camera_index = (current_camera_index + 1) % len(camera_positions)  # Alterna entre 0 e 1
    
    update_camera()
    glutPostRedisplay()


def mouse_motion(x, y):
    global angle_horizontal, angle_vertical, last_mouse_x, last_mouse_y
    
    dx = x - last_mouse_x
    dy = y - last_mouse_y

    angle_horizontal += dx * mouse_sensitivity
    angle_vertical -= dy * mouse_sensitivity

    angle_vertical = max(-89.0, min(89.0, angle_vertical))

    last_mouse_x, last_mouse_y = x, y
    glutPostRedisplay()


def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(width) / float(height), 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)


def init():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.1, 0.1, 0.1, 1.0)
    glutWarpPointer(last_mouse_x, last_mouse_y)
    glutSetCursor(GLUT_CURSOR_NONE)


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b"3D Scene with Object Descriptions")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutKeyboardFunc(keyboard)
    glutPassiveMotionFunc(mouse_motion)
    glutReshapeFunc(reshape)
    glutMainLoop()

CUBE_COLOR = random_color()
SPHERE_COLOR = random_color()
CONE_COLOR = random_color()
CYLINDER_COLOR = random_color()
TORUS_COLOR = random_color()
ICOSAHEDRON_COLOR = random_color()
DODECAHEDRON_COLOR = random_color()

if __name__ == "__main__":
    main()