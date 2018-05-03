import sys

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

GL_FRAGMENT_SHADER = 0x8B30
GL_VERTEX_SHADER = 0x8B31
GL_COMPILE_STATUS = 0x8B81
GL_LINK_STATUS = 0x8B82
GL_INFO_LOG_LENGTH = 0x8B84

def compile_shader(source, shader_type):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)

    if not glGetShaderiv(shader, GL_COMPILE_STATUS):
        raise RuntimeError(glGetShaderInfoLog(shader))

    return shader

def compile_program(vertex_source, fragment_source):
    vertex_shader = None
    fragment_shader = None
    program = glCreateProgram()

    if vertex_source:
        vertex_shader = compile_shader(vertex_source, GL_VERTEX_SHADER)
        glAttachShader(program, vertex_shader)
    if fragment_source:
        fragment_shader = compile_shader(fragment_source, GL_FRAGMENT_SHADER)
        glAttachShader(program, fragment_shader)

    glLinkProgram(program)

    if vertex_shader:
        glDeleteShader(vertex_shader)
    if fragment_shader:
        glDeleteShader(fragment_shader)

    return program









verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )

edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()






if __name__ == '__main__':
    width, height = 640, 480
    pygame.init()
    pygame.display.set_mode((width, height), OPENGL | DOUBLEBUF)

    program = compile_program('''
    // Vertex program
    varying vec3 pos;
    void main() {
        pos = gl_Vertex.xyz;
        gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
    }
    ''', '''
    // Fragment program
    varying vec3 pos;
    void main() {
        gl_FragColor.rgb = pos.xyz;
    }
    ''')

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90.0, width/float(height), 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glEnable(GL_DEPTH_TEST)
    
    quit = False
    angle = 0
    while not quit:
        for e in pygame.event.get():
            if e.type in (QUIT, KEYDOWN):
                quit = True
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glTranslate(0.0, 0.0, -2.5)
        glRotate(angle, 0.0, 1.0, 0.0)
        glUseProgram(program)
        Cube()
        angle += 0.1 
        pygame.display.flip()

