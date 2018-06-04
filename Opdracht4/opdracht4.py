#!/usr/bin/python3

import math
import glfw
import sys

from OpenGL.GL import *

import controls



# Constants
# Size of window
WINDOW_W = 640
WINDOW_H = 320
WINDOW_C = WINDOW_H if WINDOW_H < WINDOW_W else WINDOW_W
# Projection types
PROJECTION_ORTHOGRAPHIC = 1
PROJECTION_PARALLEL     = 2
PROJECTION_ISOMETRIC    = 3



# Array of current lines as tuple(x1, y1, x2, y2)
lines = []



def matrix_multiply(a, b):
    # Create empty matrix for result
    r = []
    for y in range(len(a)):
        r.append([])
        for x in range(len(b[0])):
            r[y].append(0)

    # Calculate
    for y in range(len(r)):
        for x in range(len(r[y])):
            for c in range(len(a[y])):
                r[y][x] += a[y][c] * b[c][x]

    return r



# Map coordinates to screen coordinates
def to_screen(x, y):
    # Make values positive
    x += 1
    y += 1

    # Calculate
    screen_x = (WINDOW_W / 2) - (WINDOW_C / 4) + (WINDOW_C / 2) / 2 * x
    screen_y = (WINDOW_H / 2) - (WINDOW_C / 4) + (WINDOW_C / 2) / 2 * y

    return ( screen_x, screen_y )



# Draw lines
def draw_lines():
    for line in lines:
        # Unpack line values
        ( x1, y1, x2, y2 ) = line
        ( x1, y1 ) = to_screen(x1[0], y1[0])
        ( x2, y2 ) = to_screen(x2[0], y2[0])

        # Set line color
        glColor(1, 1, 1)

        # Draw line
        glBegin(GL_LINES)
        glVertex(x1, y1)
        glVertex(x2, y2)
        glEnd()
        glFlush()



# Calculate rotation around y-axis
def rotate(cube, angle):
    rotated = []
    angle = math.radians(angle)
    for coord in cube:
        rotated.append(matrix_multiply([ [ math.cos(angle), 0, math.sin(angle) ], [ 0, 1, 0 ], [ -math.sin(angle), 0, math.cos(angle) ] ], coord))

    return rotated


# Calculate projection with projection matrix
def project(cube, projection):
    projected = []
    for coord in cube:
        if projection == PROJECTION_ORTHOGRAPHIC:
            projected.append(matrix_multiply([ [ 1, 0, 0, 0 ], [ 0, 1, 0, 0 ] ], coord))
        elif projection == PROJECTION_PARALLEL:
            projected.append(matrix_multiply([ [ 1, 0, 0.5, 0 ], [ 0, 1, 0.5, 0 ] ], coord))
        elif projection == PROJECTION_ISOMETRIC:
            projected.append(matrix_multiply([ [ 1 / math.sqrt(2), 0, 1 / math.sqrt(2), 0 ], [ 1 / math.sqrt(6), math.sqrt(2 / 3), -1 / math.sqrt(6), 0 ] ], coord))

    return projected


# Make cube coordinates into lines
def make_lines(projected):
    edges = [
        [ 1, 2 ],
        [ 2, 3 ],
        [ 3, 4 ],
        [ 4, 1 ],
        [ 1, 5 ],
        [ 2, 6 ],
        [ 3, 7 ],
        [ 4, 8 ],
        [ 5, 6 ],
        [ 6, 7 ],
        [ 7, 8 ],
        [ 8, 5 ]
    ]

    for edge in edges:
        ( x1, y1 ) = projected[edge[0] - 1]
        ( x2, y2 ) = projected[edge[1] - 1]
        lines.append(( x1, y1, x2, y2 ))



if __name__ == '__main__':
    # Initialize GLFW, exit on fail
    if not glfw.init():
        print('Failed to initialize GLFW')
        sys.exit(1)

    # Create window, exit on fail
    window = glfw.create_window(WINDOW_W, WINDOW_H, 'Opdracht 4', None, None)
    if not window:
        print('Failed to create GLFW window')
        glfw.terminate()
        sys.exit(2)

    # Tell OpenGL to use this window and show it
    glfw.make_context_current(window)

    # Set space where OpenGL can draw to
    glOrtho(0, WINDOW_W, WINDOW_H, 0, -1, 1)

    projection = PROJECTION_ORTHOGRAPHIC
    a = 0
    cube = [
        [ [ -1 ], [ -1 ], [ -1 ] ],
        [ [  1 ], [ -1 ], [ -1 ] ],
        [ [  1 ], [  1 ], [ -1 ] ],
        [ [ -1 ], [  1 ], [ -1 ] ],
        [ [ -1 ], [ -1 ], [  1 ] ],
        [ [  1 ], [ -1 ], [  1 ] ],
        [ [  1 ], [  1 ], [  1 ] ],
        [ [ -1 ], [  1 ], [  1 ] ]
    ]

    while not glfw.window_should_close(window):
        # Poll for mouse/key/other events
        glfw.poll_events()

        # Input for projection change
        if glfw.get_key(window, glfw.KEY_1) == glfw.PRESS:
            projection = PROJECTION_ORTHOGRAPHIC
        if glfw.get_key(window, glfw.KEY_2) == glfw.PRESS:
            projection = PROJECTION_PARALLEL
        if glfw.get_key(window, glfw.KEY_3) == glfw.PRESS:
            projection = PROJECTION_ISOMETRIC

        # Input for rotation
        if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            a -= 1
        if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:
            a += 1

        # Clear window and lines
        glClear(GL_COLOR_BUFFER_BIT)
        lines.clear()

        # Rotate
        rotated = rotate(cube, a)

        # Make homogeneous
        for i in range(len(rotated)):
            rotated[i].append([ 1 ])

        # Calculate projected points
        projected = project(rotated, projection)
        make_lines(projected)

        # Draw lines and controls
        draw_lines()
        controls.draw_controls()

        # Swap buffer
        glfw.swap_buffers(window)

    # Terminate GLFW
    glfw.terminate()
