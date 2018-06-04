from OpenGL.GL import *

def draw_controls():
    # Draw 1: ORTHO
    # 1
    glBegin(GL_LINE_STRIP)
    glVertex(4, 8)
    glVertex(8, 4)
    glVertex(8, 16)
    glEnd()

    # :
    glBegin(GL_POINTS)
    glVertex(12, 8)
    glVertex(12, 12)
    glEnd()

    # O
    glBegin(GL_LINE_STRIP)
    glVertex(16, 4)
    glVertex(24, 4)
    glVertex(24, 16)
    glVertex(16, 16)
    glVertex(16, 4)
    glEnd()

    # R
    glBegin(GL_LINE_STRIP)
    glVertex(28, 16)
    glVertex(28, 4)
    glVertex(36, 4)
    glVertex(36, 10)
    glVertex(28, 10)
    glVertex(36, 16)
    glEnd()

    # T
    glBegin(GL_LINE_STRIP)
    glVertex(40, 4)
    glVertex(48, 4)
    glVertex(44, 4)
    glVertex(44, 16)
    glEnd()

    # H
    glBegin(GL_LINE_STRIP)
    glVertex(52, 4)
    glVertex(52, 16)
    glVertex(52, 12)
    glVertex(60, 12)
    glVertex(60, 16)
    glVertex(60, 4)
    glEnd()

    # O
    glBegin(GL_LINE_STRIP)
    glVertex(64, 4)
    glVertex(72, 4)
    glVertex(72, 16)
    glVertex(64, 16)
    glVertex(64, 4)
    glEnd()


    # Draw 2: PARA
    # 2
    glBegin(GL_LINE_STRIP)
    glVertex(4, 24)
    glVertex(4, 20)
    glVertex(12, 20)
    glVertex(12, 24)
    glVertex(4, 32)
    glVertex(12, 32)
    glEnd()

    # :
    glBegin(GL_POINTS)
    glVertex(16, 24)
    glVertex(16, 28)
    glEnd()

    # P
    glBegin(GL_LINE_STRIP)
    glVertex(20, 32)
    glVertex(20, 20)
    glVertex(28, 20)
    glVertex(28, 26)
    glVertex(20, 26)
    glEnd()

    # A
    glBegin(GL_LINE_STRIP)
    glVertex(32, 32)
    glVertex(32, 20)
    glVertex(40, 20)
    glVertex(40, 26)
    glVertex(32, 26)
    glVertex(40, 26)
    glVertex(40, 32)
    glEnd()

    # R
    glBegin(GL_LINE_STRIP)
    glVertex(44, 32)
    glVertex(44, 20)
    glVertex(52, 20)
    glVertex(52, 26)
    glVertex(44, 26)
    glVertex(52, 32)
    glEnd()

    # A
    glBegin(GL_LINE_STRIP)
    glVertex(56, 32)
    glVertex(56, 20)
    glVertex(64, 20)
    glVertex(64, 26)
    glVertex(56, 26)
    glVertex(64, 26)
    glVertex(64, 32)
    glEnd()


    # Draw 3: ISO
    # 3
    glBegin(GL_LINE_STRIP)
    glVertex(4, 36)
    glVertex(12, 36)
    glVertex(12, 40)
    glVertex(4, 40)
    glVertex(12, 40)
    glVertex(12, 48)
    glVertex(4, 48)
    glEnd()

    # :
    glBegin(GL_POINTS)
    glVertex(16, 40)
    glVertex(16, 44)
    glEnd()

    # I
    glBegin(GL_LINE_STRIP)
    glVertex(20, 36)
    glVertex(20, 48)
    glEnd()

    # S
    glBegin(GL_LINE_STRIP)
    glVertex(32, 36)
    glVertex(24, 36)
    glVertex(24, 40)
    glVertex(32, 40)
    glVertex(32, 48)
    glVertex(24, 48)
    glEnd()

    # O
    glBegin(GL_LINE_STRIP)
    glVertex(36, 36)
    glVertex(44, 36)
    glVertex(44, 48)
    glVertex(36, 48)
    glVertex(36, 36)
    glEnd()


    # Draw arrows
    # Draw left arrow
    glBegin(GL_LINE_STRIP)
    glVertex(8, 52)
    glVertex(4, 56)
    glVertex(12, 56)
    glVertex(4, 56)
    glVertex(8, 60)
    glEnd()

    # Draw right arrow
    glBegin(GL_LINE_STRIP)
    glVertex(16, 56)
    glVertex(24, 56)
    glVertex(20, 52)
    glVertex(24, 56)
    glVertex(20, 60)
    glEnd()

    # Draw ROT
    # R
    glBegin(GL_LINE_STRIP)
    glVertex(28, 60)
    glVertex(28, 52)
    glVertex(36, 52)
    glVertex(36, 56)
    glVertex(28, 56)
    glVertex(36, 60)
    glEnd()

    # O
    glBegin(GL_LINE_STRIP)
    glVertex(40, 52)
    glVertex(48, 52)
    glVertex(48, 60)
    glVertex(40, 60)
    glVertex(40, 52)
    glEnd()

    # T
    glBegin(GL_LINE_STRIP)
    glVertex(52, 52)
    glVertex(60, 52)
    glVertex(56, 52)
    glVertex(56, 60)
    glEnd()


    glFlush()
